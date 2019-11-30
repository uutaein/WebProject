import Vue from 'vue'
import router from './router'

import BootstrapVue from "bootstrap-vue"

import App from './App'

import Default from './Layout/Wrappers/baseLayout.vue';
import Pages from './Layout/Wrappers/pagesLayout.vue';

import firebase from "firebase"

Vue.config.productionTip = false;

var config = 
{
    apiKey: "AIzaSyDXnx-Lqn8YH8UoiPv6Awetywx2wK6HGdw",
    authDomain: "webproject-6135b.firebaseapp.com",
    databaseURL: "https://webproject-6135b.firebaseio.com",
    projectId: "webproject-6135b",
    storageBucket: "webproject-6135b.appspot.com",
    messagingSenderId: "722237715982",
    appId: "1:722237715982:web:94a855e17dcd65f9306e5f",
    measurementId: "G-XHZEQ7ZCV3"
};
firebase.initializeApp(config);

Vue.use(BootstrapVue);

Vue.component('default-layout', Default);
Vue.component('userpages-layout', Pages);

new Vue({
  el: '#app',
  router,
  template: '<App/>',
  components: { App }
});
