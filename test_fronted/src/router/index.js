import Vue from 'vue'
import VueRouter from 'vue-router'
import LayOut from '../views/LayOut.vue'
import Testcase from '../views/TestCase.vue'
import Testtask from '../views/TestTask.vue'
import Testreport from '../views/TestReport.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    redirect: '/layout/testcase'
  },
  {
    path: '/layout',
    name: 'layout',
    component: LayOut,
    children:[
      {
        path: 'testcase',
        name: 'testcase',
        component: Testcase
      },
      {
        path: 'task',
        name: 'task',
        component: Testtask
      },
      {
        path: 'report',
        name: 'report',
        component: Testreport
      },
    ]
  },
]

const router = new VueRouter({
  routes
})

export default router
