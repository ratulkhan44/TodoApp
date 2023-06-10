<template>
  <div class="container mt-5">
    <div class="row">
      <div class="col-md-8">
        <div class="card">
          <div class="card-body">
              <h6>Cached:{{is_cached}}</h6>
              <table class="table" v-if="todos && todos.length">
                <thead>
                  <tr>
                    <th scope="col">Todo</th>
                    <th scope="col">Status</th>
                    <th scope="col">Action</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="todo of todos" :key="todo.id">
                    <td>{{todo.name}}</td>
                    <td v-if="todo.status">Completed</td>
                    <td v-else>Incomplete</td>
                    <td >
                      <button type="button" class="btn btn-primary btn-sm mr-2" :disabled="todo.status" @click="updateTodo(todo.id,todo.name)">Complete</button>
                      <!-- <button type="button" class="btn btn-primary btn-sm mr-2" v-else>Incomplete</button> -->
                      <button type="button" class="btn btn-danger btn-sm" @click="deletTodo(todo.id)">Delete</button>
                    </td>
                  </tr>
                </tbody>
              </table>

          </div>
        </div>
      </div>

      <div class="col-md-4">
          <form id="todo-form" method="post" @submit.prevent="postData" novalidate="true">
              <div class="form-group mt-1" v-if="alertMessage">
                  <div class="alert alert-danger"></div>
              </div>
              <div class="form-group mt-1" v-if="alertMessage">
                  <div class="alert alert-success">{{alertMessage}}</div>
              </div>
              <div class="form-group mt-3" style="text-align: left">
                  <label for="title">Name</label>
                  <input type="text" class="form-control" id="name" placeholder="Enter todo's title" v-model="todo.name"/>
              </div>
              <div class="form-group mt-3" style="text-align: left">
                  <label for="description">Status</label>
                  <select name="" class="form-control" id="status" v-model="todo.status">
                    <option :value='true'>Complete</option>
                    <option :value='false'>Incomplete</option>
                  </select>
              </div>
              <div class="form-group mt-3">
                  <button type="submit" class="btn btn-primary btn-lg btn-block">
                      Submit
                  </button>
              </div>
          </form>
      </div>
  </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      todos: [],
      errors: [],
      is_cached:false,
      todo:{
        name:null,
        status:null
      },
      alertMessage:''
    }
  },
  created() {
    this.getData()
  },
  methods:{
    getData(){
        axios.get(`http://127.0.0.1:5000`)
        .then(response => {
          // JSON responses are automatically parsed.
          this.todos = response.data.todos
          this.is_cached = response.data.is_cached
          console.log(response.data);
        })
        .catch(e => {
          this.errors.push(e)
          console.log(e)
        })
    },


    postData(e){
     axios.post(`http://127.0.0.1:5000/create_todo`,this.todo)
     .then((result) => {
      console.log(result);
      this.getData()
      this.alertMessage = "Created Successfully"
      this.todo.name =''
      this.todo.status =''
     })
     .catch(e => {
      this.errors.push(e)
      this.alertMessage = "Faild"
      console.log(e)
    })
    },

    deletTodo(id){
      axios.delete(`http://127.0.0.1:5000/delete_todo/${id}`)
      .then((result) => {
      console.log(result);
      this.getData()
      this.alertMessage = "Deleted Successfully"
     })
     .catch(e => {
      this.errors.push(e)
      this.alertMessage = "Faild"
      console.log(e)
    })
    },

    updateTodo(id,name){
      axios.put(`http://127.0.0.1:5000/update_todo/${id}`,{
        "name":name,
        "status":true
      })
      .then((result) => {
      console.log(result);
      this.getData()
      this.alertMessage = "Update Successfully"
     })
     .catch(e => {
      this.errors.push(e)
      this.alertMessage = "Faild"
      console.log(e)
    })
    },

  }
}
</script>