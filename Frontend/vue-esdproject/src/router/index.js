import { createRouter, createWebHistory } from 'vue-router'
import LandingView from '../views/LandingView.vue'
// import axios from 'axios'

const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: '/',
            name: 'landing',
            component: LandingView
        }
        // {
        //     path: '/requests',
        //     name: 'requests',
        //     // route level code-splitting
        //     // this generates a separate chunk (About.[hash].js) for this route
        //     // which is lazy-loaded when the route is visited.
        //     component: () => import('../views/RequestView.vue')
        // }
    ]
})

export default router
