import { createStore } from 'vuex'
import axios from 'axios'


export default createStore({
  state: {
    tasks: []
  }, 
  mutations: {
    updateTasks (state, tasks){
      state.tasks = tasks
    },
    deleteTasks (state, task){
      state.tasks.splice(state.tasks.indexOf(task), 1)
    }
  },
  actions: {
    fetchTasks({commit}){
      axios
        .get('tasks/')
        .then(r =>  r.data)
        .then(tasks => {
          commit('updateTasks', tasks)
      })    
    },
    deleteTask({commit}, task){
      axios
        .delete('tasks/' + task.id)
        .then(r =>  r.data)
        .then(tasks => {
          commit('deleteTasks', tasks)
        })
    }
  },
  modules: {
  },
  getters: {
    allTasks(state){
      return state.tasks.sort((x, y)=>{
        if(x == y){
          return 0
        }
        if(x){
          return 1
        }
        else{
          return -1
        }
      })
    }
  }
})
