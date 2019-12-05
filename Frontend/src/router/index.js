import Vue from 'vue'
import Router from 'vue-router'
import firebase from "firebase";

Vue.use(Router);

export default new Router({
    scrollBehavior() {
        return window.scrollTo({ top: 0, behavior: 'smooth' });
    },
    mode:'history',
    routes: [

        //Dashboards
        {
            path: '/Dashboards',
            name: 'analytics',
            component: () => import('../Layout/Components/Dashboards/Analytics.vue'),
        },      
            

        // Login
        {
            path: '/',
            name: 'login',
            meta: {layout: 'userpages'},
            component: () => import('../Layout/Components/LoginBoxed.vue'),
        },
        {
            path: '/Register',
            name: 'register-boxed',
            meta: {layout: 'userpages'},
            component: () => import('../Layout/Components/RegisterBoxed.vue'),
        },
        {
            path: '/pages/Chart',
            name : 'Chart',
            component:()=>import('../Layout/Components/Chart.vue'),
        },
        {
            path: '/pages/Strategy-Simulator',
            name : 'Strategy Simulator',
            component:()=>import('../Layout/Components/StrategySimulator.vue'),
        },
        {
            path: '/pages/Stat-Strategy',
            name : 'Stat Strategy',
            component:()=>import('../Layout/Components/StatStrategy.vue'),
        },
        {
            path: '/pages/Investment-Game',
            name : 'InvestmentGame',
            component:()=>import('../Layout/Components/InvestmentGame.vue'),
        },
        
        
    ]
})
