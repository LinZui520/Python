import {createRouter, createWebHistory} from "vue-router"
import Home from "../views/Home.vue"

const routes = [
    {
        path:"/",
        // redirect:"/home"
        redirect:"/login"
    },
    {
        path:"/home",
        name:"home",
        component:Home,
    },
    {
        path:"/login",
        name:"login",
        component: () => import('../views/Login.vue')
    },
    {
        path:"/register",
        name:"register",
        meta:{
            requiresAuth: true
        },
        component: () => import('../views/Register.vue')
    },
    {
        path:"/:userName",
        name:"account",
        component: () => import('../views/Account.vue')
    },
    {
        path: '/404',
        name: 'NotFound',
        meta:{
            requiresAuth:false
        },
        component: () => import('../components/NotFound.vue'),
    },
      // 所有未定义路由，全部重定向到404页
    {
        path: "/:pathMatch(.*)",
        redirect: '/404',
    }
];

const router = createRouter({
    history: createWebHistory(),	
    routes, 
});

export default router