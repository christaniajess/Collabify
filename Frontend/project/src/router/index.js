import { createRouter, createWebHistory } from 'vue-router';
import AppLayout from '@/layout/AppLayout.vue';

const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: '/',
            component: AppLayout,
            children: [
                {
                    path: '/',
                    name: 'dashboard',
                    component: () => import('@/views/Dashboard.vue')
                },


                {
                    path: '/collab',
                    name: 'collab',
                    component: () => import('@/views/pages/Collab.vue')
                },
                {
                    path: '/blacklist',
                    name: 'blacklist',
                    component: () => import('@/views/pages/Blacklist.vue')
                },
                {
                    path: '/brandsearch',
                    name: 'brandsearch',
                    component: () => import('@/views/pages/BrandSearchCC.vue')
                },

                {
                    path: '/payment',
                    name: 'payment',
                    component: () => import('@/views/pages/Payment.vue')
                },

                {
                    path: '/request',
                    name: 'request',
                    component: () => import('@/views/pages/Request.vue')
                },

                {
                    path: '/viewprojects',
                    name: 'viewprojects',
                    component: () => import('@/views/pages/CCViewProjects.vue')
                },
                {
                    path: '/viewccprofile',
                    name: 'viewccprofile',
                    component: () => import('@/views/pages/BrandViewCC.vue')
                },
                {
                    path: '/profile',
                    name: 'profile',
                    component: () => import('@/views/pages/profile.vue')
                },
            ]
        },

        {
            path: '/login',
            name: 'login',
            component: () => import('@/views/auth/Login.vue')
        },
        
        {
            path: '/logout',
            name: 'logout',
            component: () => import('@/views/auth/Logout.vue')
        }
    ]
});

export default router;
