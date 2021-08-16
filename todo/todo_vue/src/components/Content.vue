<template>
    <div class="q-pa-md" style="max-width: 350px">
        <q-list bordered separator overline>
            <q-item clickable v-for="task in allTasks" :key="task.id" v-bind:class="classState(task.is_active)" v-ripple>
                <q-item-section overline>
                    <q-item-label>{{task.title}}</q-item-label>
                    <q-item-label>{{task.details}}</q-item-label>
                </q-item-section>
                    <q-item-section top side>
                    <q-btn v-on:click="deleteTask(task)" class="gt-xs" size="12px " flat dense round icon="delete"/>
                </q-item-section>
            </q-item>
        </q-list>
    </div>
</template>

<script>
import {mapGetters, mapActions} from 'vuex'

export default {
    name: 'Content',
    methods: {
        ...mapActions(['fetchTasks', 'deleteTask']),
        classState: function(isActive){
            if(isActive) return 'active'
            else return 'completed'
        },

    },
    computed: mapGetters([
        'allTasks'
    ]),
    mounted(){
        this.fetchTasks('fetchTasks')
    }
}
</script>
