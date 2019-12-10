<template>
    <div id="StrategySimulator">
        <h1>
            주식 종목 길잡이<br>
            <small>스탯을</small>
        </h1>
        <div>
            <p>포트폴리오를 입력하세요</p>
            <hr>
            <p>시작날짜를 선택하세요</p>
            <input v-model="date" type="date" placeholder="날짜" @change="datechangeInit">
            <p>초기자본금을 설정하세요(단위 : 만원)</p>
            <input v-model="budget" type="number" placeholder="초기자본금 설정"><hr>
            <b-button variant="outline-info" @click="addStock" size="sm">종목추가</b-button>
            <b-button variant="outline-danger" @click="deleteStock" size="sm">종목삭제</b-button>
            <div v-for="(idx,i) in stockNum" class="row" >
                {{passer(i)}}
                <!-- <label for="stockCode">종목코드</label>
                <select id="stockCode" v-model="stockCode[i]">
                    <option v-for="idx in stockList" v-bind:value="idx.code">코드:{{idx.code}} /종목명:{{idx.name}} /상장일자:{{idx.date}}</option>
                </select> -->
                <div class="position-relative form-group">
                                    <model-select :options="options" v-model="stockCode[i]" placeholder="주식을 선택해주세요" style="width : 250px;">
                                    </model-select>
                </div>
                  <div class="position-relative form-group" style="width : 100px;">
                <input v-model="ratio[i]" type="number" placeholder="비중(%)">
                </div>
            </div>
            <br>
            <b-button variant="success" @click="validation" size="sm">입력완료</b-button>
        </div>

         <div class="col-sm-12 col-lg-6" v-if="valid">
                <div class="mb-3 card">
                    <div class="card-header-tab card-header">
                        <div class="card-header-title font-size-lg text-capitalize font-weight-normal">
                            <i class="header-icon lnr-cloud-download icon-gradient bg-happy-itmeo"> </i>
                            내 포트폴리오 결과
                        </div>
                    </div>
                    <div class="p-0 card-body">
                        <div class="p-1 slick-slider-sm mx-auto">
                            <div class="widget-chart widget-chart2 text-left p-0">
                                <div class="widget-chat-wrapper-outer">
                                    <div class="widget-chart-content widget-chart-content-lg pb-0">

                                        <div class="widget-chart-flex">
                                            <div class="widget-title opacity-5 text-muted text-uppercase">최종 수익률
                                            </div>
                                        </div>
                                        <div class="widget-numbers">
                                            <div class="widget-chart-flex">
                                                <div>
                                                    <span class="text-warning">{{ this.$store.state.SS_whole_profit }}%</span>
                                                </div>
                                            </div>
                                        </div>

                                        <div class="widget-chart-flex">
                                            <div class="widget-title opacity-5 text-muted text-uppercase">연환산 수익률
                                            </div>
                                        </div>
                                        <div class="widget-numbers">
                                            <div class="widget-chart-flex">
                                                <div>
                                                    <span class="text-warning">{{ this.$store.state.SS_annual_profit }}%</span>
                                                </div>
                                            </div>
                                        </div>

                                    </div>
                                    <div class="widget-chart-wrapper he-auto opacity-10 m-0">
                                        <SSchart :height="145" v-if="this.$store.state.SS_chart_done"/>
                                    </div>
                                </div>
                            </div>
                        </div>

                        
                    </div>
                </div>
         </div>
            
    </div>
</template>

<script>
    import SSchart from './Analytics/SS_chart1';
    import VuePerfectScrollbar from 'vue-perfect-scrollbar';
    import firebase from 'firebase'
    import { ModelSelect } from 'vue-search-select'
    import 'vue-search-select/dist/VueSearchSelect.css'
    export default {
        components: {
            VuePerfectScrollbar,
            SSchart,
            ModelSelect
        },
        name: "StrategySimulator",
        data(){
            return{
                stockNum:[],
                date:'',
                budget: 0,
                stockCode: [],
                stockList: [],
                ratio: this.$store.state.SS_ratio,
                tmp:0,
                valid:false,
                options:[]

            }
        },
        methods:{
            addStock:function () {
                //종목추가
                if(this.date=='') {
                    alert('날짜를 먼저 선택해주세요')
                    return
                }
                else {
                    this.stockNum.push(null);
                    if(this.stockList.length==0) {
                        console.log(this.date)
                        this.$axios.get('test/SS/'+this.date).then(response=>{
                            this.stockList=response.data;
                            for(var i=0;i<this.stockList.length;i++){
                             this.options.push({text: this.stockList[i].name,
                                        value:this.stockList[i].code})
                        }
                        })
                    }
                }
            },
            deleteStock:function () {
                //종목삭제할때 input값 초기화할때 쓰는 함수
                this.ratio[this.tmp]=''
                this.stockNum.pop();
            },
            passer:function (i) {
                //종목삭제할때 input값 초기화할때 쓰는 함수
                this.tmp=i;
            },
            validation:function () {
                //입력완료 눌렀을때 비중입력 총합 100이하인지 확인하는 함수
                var a = 0;
                for(var i=0;i<this.ratio.length;i++) {
                    a += Number(this.ratio[i]);
                }
                if(a!=100){
                    alert('비중의 총합이 100이 되도록 재설정하세요.')
                    return false
                }
                else{
                    this.valid=true;
                    this.$store.state.SS_init_money = this.budget;
                    this.$store.dispatch('calculatePortfolio',{date:this.date,stockCode:this.stockCode,ratio:this.ratio});
                    //validation하고 맞으면 입력받은 date랑 stockCode를 back으로 보내

                }
            },
            datechangeInit: function () {
                this.stockNum.splice(0,this.stockNum.length);
                this.stockList.splice(0,this.stockList.length);
                this.stockCode.splice(0,this.stockCode.length);
                this.ratio.splice(0,this.ratio.length);
                this.valid=false;
            },
            saveDataInFB: function () {

            }
        }
    }
</script>

<style scoped>

.inputContainer{
    margin-top: 10px;
}
    input{
         margin-right: 10px;
    }
    select{
        margin-right: 10px;
    }
</style>