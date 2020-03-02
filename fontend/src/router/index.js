import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home/index.vue'

Vue.use(VueRouter)

//公共路由
const routes = [
  {
    path: '/',
    name: 'Home',
	component: Home,
	redirect: '/dashboard',
	name: '',
	leaf: true,
	children: [
		{
			path: '/dashboard',
			component: () => import('../views/Dashboard/index.vue')
		}
	]
    
  },

  {
    path: '/',
    component: Home,
    name: '',
    leaf: true,
    children: [
      {
        path: '/cases',
        component: () => import('../views/Cases/index.vue')
      }
    ]
  },
  
  {
    path: '/',
    component: Home,
    name: '',
    leaf: true,
    children: [
      {
        path: '/news',
        component: () => import('../views/News/index.vue')
      }
    ]
  },
  
  {
    path: '/',
    component: Home,
    name: '',
    leaf: true,
    children: [
      {
        path: '/blacklist',
        component: () => import('../views/Blacklist/index.vue')
      }
    ]
  },
  
]



const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
