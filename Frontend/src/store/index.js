import Vue from 'vue'
import Vuex from 'vuex'
import axios from '../plugins/axios.js'
Vue.use(Vuex);

export default new Vuex.Store({
    state :
    {
        chart1_labels : [],
        chart1_data : [],
        
        SS_init_money : 1000000,
        SS_init_stocks : [],
        SS_init_index_stock_num : 0,
        SS_ratio : [],
        SS_chart_labels : [],
        SS_chart_data1 : [],
        SS_chart_data2 : [],
        SS_chart_done : false
    },
    // 전체돈 * ration / 주식개별  
    // 전체돈 * 코스닥 가격  
    /**
   * Mutation is the simple state-changing operation
   * that does not contain other Frontend logic and AJAX requests.
   * */
    mutations :
    {
        //From : https://kamang-it.tistory.com/entry/Vue17vuex-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0actions%EB%A1%9C-%EB%B9%84%EB%8F%99%EA%B8%B0-%ED%86%B5%EC%8B%A0
        addDataToChartSuccess(state, payload)
        {   
            for(var i=payload.data.length-1; i>=0; i--)
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
        },

        calculatePortfolioSuccess(state, payload)
        {
            //살 종목의 개수 + 1(코스피)
            var payloadSize = payload.data.length-1;
            //날짜의 개수
            var payloadNumSize = payload.data[payloadSize].length -1;


            //첫날 코스피 산 개수
            state.SS_init_index_stock_num = state.SS_init_money / payload.data[payloadSize][0].close;
            console.log(state.SS_init_index_stock_num);

            for(var i=0; i<=payloadNumSize; i++)
            {
                var tdate = payload.data[payloadSize][i].date
                state.SS_chart_labels.push(tdate);

                var tvalue = state.SS_init_index_stock_num * payload.data[payloadSize][i].close;
                state.SS_chart_data1.push(tvalue);
            }
            //날짜, 코스피 지수 차트저장 완료
            console.log(state.SS_chart_data1);

            for(var i=0; i<=payloadNumSize; i++)
            {
                state.SS_chart_data2.push(Number(0));
            }

            // 초기 구매 주식 개수
            for(var i=0; i<payloadSize; i++)
            {
                var tinit_stocks = state.SS_init_money*state.SS_ratio[i] / payload.data[i][payloadNumSize].close/100;
                state.SS_init_stocks.push(tinit_stocks);
            }
            console.log(state.SS_init_stocks);

            // 포트폴리오 변동 계산.
            for(var i=0; i<=payloadNumSize; i++)
            {
                for(var j=0; j<payloadSize; j++)
                {
                    state.SS_chart_data2[i] += Number(state.SS_init_stocks[j] * payload.data[j][i].close);
                }
            }
            state.SS_chart_data2.reverse();
            state.SS_chart_done = true;
            console.log(state.SS_chart_data2);
        },
        calculatePortfolioFail(state, payload)
        {
            console.log(payload);
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
            .catch((err) => {
                commit('addDataToChartFail',err);
            });
        },
        calculatePortfolio({commit},payload)
        {
            axios.post('/test/api',payload)
                .then((res) => {
                    commit('calculatePortfolioSuccess',res);
                })
                .catch((err) => {
                    commit('calculatePortfolioFail',err);
                });
        }

    },
    modules :
    {

    }


});