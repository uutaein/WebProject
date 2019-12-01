import Vue from 'vue'
import Vuex from 'vuex'
import axios from '../plugins/axios.js'
Vue.use(Vuex);

export default new Vuex.Store({
    state :
    {
        chart1_labels : [],
        chart1_data : [],
    },

    /**
   * Mutation is the simple state-changing operation
   * that does not contain other Frontend logic and AJAX requests.
   * */
    mutations :
    {
        //From : https://kamang-it.tistory.com/entry/Vue17vuex-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0actions%EB%A1%9C-%EB%B9%84%EB%8F%99%EA%B8%B0-%ED%86%B5%EC%8B%A0
        addDataToChartSuccess(state, payload)
        {
            for(var i=0; i<payload.data.length; i++)
            {
                var tdate = payload.data[i].date;
                state.chart1_labels.push(tdate);

                var tvalue = payload.data[i].high;
                state.chart1_data.push(tvalue);
            }
        },
        addDataToChartFail(/*state, payload*/)
        {
            console.log('addDataToChart Error!');
        }
    },
    actions :
    {
       addDataToChart({commit})
        {
           axios.post('test',{start:this.start})
            .then((res) => {
                commit('addDataToChartSuccess',res);
            })
            .catch((res) => {
                commit('addDataToChartFail',res);
            });
        }
        
    },
    modules :
    {

    }


});