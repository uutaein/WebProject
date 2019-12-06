import Vue from 'vue'
import axios from 'axios'


const firebaseAPI = axios.create({
    //baseURL : 'https://us-central1-webproject-6135b.cloudfunctions.net/',
    baseURL : 'http://localhost:5000/webproject-6135b/us-central1/',
    timeout : 100000,
    headers : {'X-Custom-Header' : 'foobar'}
});

Vue.prototype.$axios = firebaseAPI

export default firebaseAPI