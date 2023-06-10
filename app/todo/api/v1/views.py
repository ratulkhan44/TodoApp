from urllib import response
from flask import Blueprint, request, jsonify
from flask_cors import cross_origin
from db_init import db
from todo.api.models import Todo
from redis import Redis
import json

api_views = Blueprint("views", __name__)
redis_host = 'localhost'
redis_port = 6379
redis_db = 1
redis_client = Redis(host=redis_host, port=redis_port, db=redis_db)

@api_views.route('/create_todo',methods=["POST"])
@cross_origin(origin='*',headers=['Content-Type'])
def create_todo():
    print("assssssssssss",request)
    if request.method == "POST":
        try:
            if not request.data:
                raise Exception("Valid data is required")
            
            is_cached = False


            name = request.json.get("name", None)
            status = request.json.get("status", None)
            new_todo= Todo(name=name,
                                status=status)
            

            db.session.add(new_todo)
            db.session.commit()
            todo_list  = []

            todo_data = { 
                    "id":int(new_todo.id),
                    "name":name,
                    "status":status
                }
            if redis_client.exists('todo_list'):
                get_todo_from_redis = json.loads(redis_client.get('todo_list'))
                print("="*30)
                print("================== REdis ============",get_todo_from_redis)

                get_todo_from_redis.append(todo_data)
                redis_client.delete('todo_list')
                redis_client.set("todo_list",json.dumps(get_todo_from_redis))
            else:
                todo_list.append(todo_data)

                redis_client.set('todo_list',json.dumps(todo_list))

                print("*"*20,json.loads(redis_client.get('todo_list')))

            # print("dsdsdsds",get_todo_from_redis)

            # if get_todo_from_redis is not None:
            #     get_todo_from_redis.append(save_data)
            #     data = json.dumps(get_todo_from_redis)
            #     redis_client.set('todo',data)
            #     is_cached = True

            # my_list.append[save_data]
            # data = json.dumps(my_list)
            # redis_client.set('todo',data)

            # print("================== REdis ============",eval(get_todo_from_redis))

            response = {
                "StatusCode": 200,
                "message": "Successfully Creted",
                "is_cached": is_cached,
                "todo": {
                   "name":name,
                   "status":status
                },
            }
            return jsonify(response)
        except Exception as exp:
            return jsonify({"StatusCode": 400, "message": str(exp)})
        

@api_views.route('/',methods=["GET"])
@cross_origin(origin='*',headers=['Content-Type'])
def todo_list():
    try:
        is_cached = False
        todos = None
        if redis_client.exists('todo_list'):
            todos = json.loads(redis_client.get('todo_list'))
            print("todos",todos)
            is_cached = True
        else:
            print("============== Iside")
            todo_list = Todo.query.all()

            serialized_data = []
            for item in todo_list:
                serialized_data.append({
                    "id":item.id,
                    'name': item.name,
                    'status': item.status,
                    # Add more fields as needed
                })
            redis_client.set('todo_list',json.dumps(serialized_data))
            todos = serialized_data

        response = {
            "StatusCode": 200,
            "is_cached": is_cached,
            "todos":todos
        }
        return jsonify(response)

    except Exception as exp:
            return jsonify({"StatusCode": 400, "message": str(exp)})
    
@api_views.route('/update_todo/<int:todo_id>',methods=['PUT'])
def update_todo(todo_id):
    if request.method == "PUT":
        try:
            if not request.data:
                raise Exception("Valid data is required")
            name = request.json.get("name", None)
            status = request.json.get("status", None)

            todo = Todo.query.get(todo_id)
            todo.name = name
            todo.status = status
            db.session.commit()

            if redis_client.exists('todo_list'):
                # todos = Todo.query.all()
                redis_client.delete('todo_list')
                # redis_client.set('todo_list',json.dumps(todos))

                todo_list = Todo.query.all()

                serialized_data = []
                for item in todo_list:
                    serialized_data.append({
                        "id":item.id,
                        'name': item.name,
                        'status': item.status,
                        # Add more fields as needed
                    })
                redis_client.set('todo_list',json.dumps(serialized_data))


            response = {
                "StatusCode": 200,
                "message": "Successfully Updated",
                "todo": {
                   "name":name,
                   "status":status
                },
            }
            return jsonify(response)
        except Exception as exp:
            return jsonify({"StatusCode": 400, "message": str(exp)})
        

@api_views.route('/delete_todo/<int:todo_id>',methods=['DELETE'])
def delete_todo(todo_id):
    if request.method == "DELETE":
        try:

            todo = Todo.query.get(todo_id)
            db.session.delete(todo)
            db.session.commit()

            if redis_client.exists('todo_list'):
                # todos = Todo.query.all()
                redis_client.delete('todo_list')
                # redis_client.set('todo_list',json.dumps(todos))

                redis_client.delete('todo_list')
                # redis_client.set('todo_list',json.dumps(todos))

                todo_list = Todo.query.all()

                serialized_data = []
                for item in todo_list:
                    serialized_data.append({
                        "id":item.id,
                        'name': item.name,
                        'status': item.status,
                        # Add more fields as needed
                    })
                redis_client.set('todo_list',json.dumps(serialized_data))

            response = {
                "StatusCode": 200,
                "message": "Successfully Deleted"
            }
            return jsonify(response)
        except Exception as exp:
            return jsonify({"StatusCode": 400, "message": str(exp)})
