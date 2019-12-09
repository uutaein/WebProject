import Vue from 'vue'
import Vuex from 'vuex'
import axios from '../plugins/axios.js'
Vue.use(Vuex);

export default new Vuex.Store({
    state :
    {
        chart1_labels : [],
        chart1_data : [],
        
        IG_init_money : 0,
        IG_result_money : 0,
        IG_init_date : '',
        IG_init_stocks : [],
        IG_init_index_stock_num : 0,
        IG_init_kospi_stock_num : 0,
        IG_ratio : [],
        IG_chart_labels : [],
        IG_chart_data1 : [],
        IG_chart_data2 : [],
        IG_chart_done : false,
        IG_profit : 0,
        IG_max_profit : 0,
        IG_chart_total_labels : [],
        IG_chart_total_data1 : [],
        IG_chart_total_data2 : [],
        IG_chart_total_done : false,
        IG_net_money: 0,
        IG_total_net_money : 0,
        IG_total_net_profit : 0,

        SS_init_money : 0,
        SS_init_stocks : [],
        SS_init_index_stock_num : 0,
        SS_ratio : [],
        SS_chart_labels : [],
        SS_chart_data1 : [],
        SS_chart_data2 : [],
        SS_chart_done : false,

        //총 투자 수익률
        SS_whole_profit : 0,

        //연환산 수익률
        SS_annual_profit : 0
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
            

                var tvalue = payload.data[i].high;
            }
        },
        addDataToChartFail(/*state, payload*/)
        {
            console.log('addDataToChart Error!');
        },

        calculatePortfolioSuccess(state, payload)
        {
            this.state.SS_init_money *= 10000;
            //살 종목의 개수 + 1(코스피)
            var payloadSize = payload.data.length-1;
            
            //투자 일수
            var payloadNumSize = payload.data[payloadSize].length -1;
          
            //연환산 투자 기간
            var investDuration = payloadNumSize/365;
            investDuration = investDuration.toFixed(2);

            //첫날 코스피 산 개수
            state.SS_init_index_stock_num = this.state.SS_init_money / payload.data[payloadSize][0].close;
            

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
            state.SS_whole_profit = (state.SS_chart_data2[payloadNumSize] - state.SS_init_money ) / state.SS_init_money * 100;
            state.SS_whole_profit = state.SS_whole_profit.toFixed(3)

            //연환산 수익률
            //(1+기간수익률)^(1/연환산투자기간)-1
            state.SS_annual_profit = Math.pow((1+state.SS_whole_profit/100),(1/investDuration)) -1;
            state.SS_annual_profit = (state.SS_annual_profit*100).toFixed(3);
            //alert(state.SS_annual_profit);

            state.SS_chart_done = true;
            //console.log(state.SS_chart_data2);
        },
        calculatePortfolioFail(state, payload)
        {
            console.log(payload);
        },
        IGcalculatePortfolioSuccess(state, payload)
        {
            
            //살 종목의 개수 + 1(코스피)
            var payloadSize = payload.data.length-1;
            //날짜의 개수
            var payloadNumSize = payload.data[payloadSize].length -1;
            
            //이미 차트가 그려졌던 경우.
            var startmoney;
            if(state.IG_result_money == 0)
            {
                startmoney = state.IG_init_money;
                state.IG_init_kospi_stock_num = startmoney / payload.data[payloadSize][0].close;
            }
            else
            {
                startmoney = state.IG_result_money;
            }

            //첫날 코스피 산 개수
            state.IG_init_index_stock_num = startmoney / payload.data[payloadSize][0].close;
            //console.log(state.IG_init_index_stock_num);

            for(var i=0; i<=payloadNumSize; i++)
            {
                var tdate = payload.data[payloadSize][i].date
                state.IG_chart_labels.push(tdate);
                state.IG_chart_total_labels.push(tdate);

                var tvalue = state.IG_init_index_stock_num * payload.data[payloadSize][i].close;
                state.IG_chart_data1.push(tvalue);

                var t_total_value = state.IG_init_kospi_stock_num * payload.data[payloadSize][i].close;
                state.IG_chart_total_data1.push(t_total_value);
            }
            //날짜, 코스피 지수 차트저장 완료
            //console.log(state.IG_chart_data1);
            
            for(var i=0; i<=payloadNumSize; i++)
            {
                state.IG_chart_data2.push(Number(0));
            }

            // 초기 구매 주식 개수
            for(var i=0; i<payloadSize; i++)
            {
                var tinit_stocks = startmoney*state.IG_ratio[i] / payload.data[i][payloadNumSize].close/100;
                state.IG_init_stocks.push(tinit_stocks);
            }
            //console.log(state.IG_init_stocks);

            // 포트폴리오 변동 계산.
            for(var i=0; i<=payloadNumSize; i++)
            {
                for(var j=0; j<payloadSize; j++)
                {
                    state.IG_chart_data2[i] += Number(state.IG_init_stocks[j] * payload.data[j][i].close);
                }
            }
            state.IG_result_money = state.IG_chart_data2[0];
            state.IG_chart_data2.reverse();
            state.IG_chart_total_data2 = state.IG_chart_total_data2.concat(state.IG_chart_data2);

        
            state.IG_profit = (state.IG_chart_data2[payloadNumSize] - startmoney ) / startmoney * 100;
            state.IG_net_money = state.IG_chart_data2[payloadNumSize] - startmoney;
            if(state.IG_max_profit <= state.IG_profit)
            {
                state.IG_max_profit = state.IG_profit;
            }
            var total_data_length = state.IG_chart_total_data2.length - 1;
            state.IG_total_net_money =  state.IG_chart_total_data2[total_data_length] - state.IG_init_money;
            state.IG_total_net_profit =  (state.IG_chart_total_data2[total_data_length] - state.IG_init_money) / state.IG_init_money * 100;
            state.IG_chart_done = true;
            state.IG_chart_total_done = true;
    },
        IGcalculatePortfolioFail(state, payload)
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
            axios.post('test/api',payload)
                .then((res) => {
                    commit('calculatePortfolioSuccess',res);
                })
                .catch((err) => {
                    commit('calculatePortfolioFail',err);
                });
        },
        IGcalculatePortfolio({commit},payload)
        {
            axios.post('test/apitest',payload)
                .then((res) => {
                    commit('IGcalculatePortfolioSuccess',res);
                })
                .catch((err) => {
                    commit('IGcalculatePortfolioFail',err);
                });
        },

    },
    modules :
    {

    }


});