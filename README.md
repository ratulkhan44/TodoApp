
##### Prerequisite
1. This project is tested in Ubuntu 20.04.3 LTS
2. Python 3.8.10
3. Nodejs 18.16.0

##### Installation Guide
1. Create a Directory
```bash
mkdir directory name
cd directory name
```

2. From source:

```bash
git clone https://github.com/example.git
```

3. Create Python Environment:
```bash
python3 -m venv env
```
4. Activate Environment
```bash
source env/bin/activate
```
5. Change Directory
```bash
cd app
```
5. Install requirements.txt
```bash
pip3 install -r requirements.txt
```
6. Run main.py
```bash
python3 -m main.py
```
7. Open http://127.0.0.1:5000

8. Change Directory
```bash
cd app
```
9. Install npm
```bash
npm install
```
10. Run The Project
```bash
npm run dev 

11. Open http://127.0.0.1:5173


 ##### Api Details

###### Create Todo

```End Point```: ```/create_todo``` <br>
```Request Method```: ```Post``` <br>
```Args Example: ```
```
{
    "name":"This is my todo",
    "status":false
}
```
```Sucecessful Response: ```
```
```
{
    "StatusCode": 200,
    "is_cached": false,
    "message": "Successfully Creted",
    "todo": {
        "name": "this is anpther todo",
        "status": false
    }
}
```

```Unsuccessful Response: ```
```
{
    "StatusCode": 400,
    "message": "Valid data is required"
}
```


###### Get All Todos

```End Point```: ```/``` <br>
```Request Method```: ```Get``` <br>

```Sucecessful Response: ```
```
{
    "StatusCode": 200,
    "is_cached": false,
    "todos": [
        {
            "id": 1,
            "name": "First todo",
            "status": false
        },
        {
            "id": 3,
            "name": "Second Todo",
            "status": false
        }
    ]
}
```

```Unsuccessful Response: ```
```
{
    "StatusCode": 400,
    "message": "Valid data is required"
}
```
###### Update specific Todos

```End Point```: ```/update_todo/<int:id>``` <br>
```Request Method```: ```Put``` <br>

```Sucecessful Response: ```
```
{
    "StatusCode": 200,
    "message": "Successfully Updated",
    "todo": {
        "name": "this is updated todo",
        "status": true
    }
}
```

```Unsuccessful Response: ```
```
{
    "StatusCode": 400,
    "message": "Raised error"
}
```
###### Delete Todo

```End Point```: ```/delete_todo/<int:id>``` <br>
```Request Method```: ```Delete``` <br>

```Sucecessful Response: ```
```
{
    "StatusCode": 200,
    "message": "Successfully Deleted"
}
```

```Unsuccessful Response: ```
```
{
    "StatusCode": 400,
    "message": "Raised error"
}
```
