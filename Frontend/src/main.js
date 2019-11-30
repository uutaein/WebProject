import Vue from 'vue'
import router from './router'

import BootstrapVue from "bootstrap-vue"

import App from './App'

import Default from './Layout/Wrappers/baseLayout.vue';
import Pages from './Layout/Wrappers/pagesLayout.vue';

import firebase from "firebase";
import './plugins/axios';
Vue.config.productionTip = false;

var config = 
{
    apiKey: "AIzaSyCdKZCyU4RDdjECSPt7QHusuyoQg3ZKKD0",
    authDomain: "wsdtp-4aa53.firebaseapp.com",
    databaseURL: "https://wsdtp-4aa53.firebaseio.com",
    projectId: "wsdtp-4aa53",
    storageBucket: "wsdtp-4aa53.appspot.com",
    messagingSenderId: "100505156541",
    appId: "1:100505156541:web:0b87e7e0532b4b8ec830d4",
    measurementId: "G-QBJZQM117X"
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
