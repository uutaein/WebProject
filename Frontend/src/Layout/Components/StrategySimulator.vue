<template>
    <div id="StrategySimulator">
        <h1>
            전략시뮬레이터<br>
            <small>포트폴리오 성과추출기</small>
        </h1>
        <div>
            <p>포트폴리오를 입력하세요</p>
            <hr>
            <p>시작날짜를 선택하세요</p>
            <input v-model="date" type="date" placeholder="날짜" @change="datechangeInit">
            <p>초기자본금을 설정하세요(단위 : 만원)</p>
            <input v-model="budget" type="number" placeholder="초기자본금 설정"><hr>
            <button @click="addStock">종목추가</button>
            <button @click="deleteStock">종목삭제</button>
            <div v-for="(idx,i) in stockNum" class="inputContainer" >
                {{passer(i)}}
                <label for="stockCode">종목코드</label>
                <select id="stockCode" v-model="stockCode[i]">
                    <option v-for="idx in stockList" v-bind:value="idx.code">코드:{{idx.code}} /종목명:{{idx.name}} /상장일자:{{idx.start_date}}</option>
                </select>
                <input v-model="ratio[i]" type="number" placeholder="비중(%)">
            </div>
            <br>
            <button @click="validation">입력완료</button>
        </div>

         <div class="col-sm-12 col-lg-6">
                <div class="mb-3 card">
                    <div class="card-header-tab card-header">
                        <div class="card-header-title font-size-lg text-capitalize font-weight-normal">
                            <i class="header-icon lnr-cloud-download icon-gradient bg-happy-itmeo"> </i>
                            Technical Support
                        </div>
                    </div>
                    <div class="p-0 card-body">
                        <div class="p-1 slick-slider-sm mx-auto">
                            <div class="widget-chart widget-chart2 text-left p-0">
                                <div class="widget-chat-wrapper-outer">
                                    <div class="widget-chart-content widget-chart-content-lg pb-0">
                                        <div class="widget-chart-flex">
                                            <div class="widget-title opacity-5 text-muted text-uppercase">Helpdesk
                                                Tickets
                                            </div>
                                        </div>
                                        <div class="widget-numbers">
                                            <div class="widget-chart-flex">
                                                <div>
                                                    <span class="text-warning">34</span>
                                                </div>
                                                <div
                                                    class="widget-title ml-2 font-size-lg font-weight-normal text-dark">
                                                    <span class="opacity-5 text-muted pl-2 pr-1">5%</span>
                                                    increase
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="widget-chart-wrapper he-auto opacity-10 m-0">
                                        <chart1 :height="145"/>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <h6 class="text-muted text-uppercase font-size-md opacity-5 pl-3 pr-3 pb-1 font-weight-normal">
                            Sales Progress</h6>
                        <ul class="list-group list-group-flush">
                            <li class="p-3 bg-transparent list-group-item">
                                <div class="widget-content p-0">
                                    <div class="widget-content-outer">
                                        <div class="widget-content-wrapper">
                                            <div class="widget-content-left">
                                                <div class="widget-heading">Total Orders</div>
                                                <div class="widget-subheading">Last year expenses</div>
                                            </div>
                                            <div class="widget-content-right">
                                                <div class="widget-numbers text-success">
                                                    <small>$</small>
                                                    1896
                                                </div>
                                            </div>
                                        </div>
                                        <div class="widget-progress-wrapper">
                                            <div class="progress-bar-sm progress-bar-animated-alt progress">
                                                <div class="progress-bar bg-primary" role="progressbar"
                                                     aria-valuenow="43" aria-valuemin="0" aria-valuemax="100"
                                                     style="width: 43%;"></div>
                                            </div>
                                            <div class="progress-sub-label">
                                                <div class="sub-label-left">YoY Growth</div>
                                                <div class="sub-label-right">100%</div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
    </div>
</template>

<script>
    import chart1 from './Dashboards/Analytics/chart1';
    import VuePerfectScrollbar from 'vue-perfect-scrollbar';

    export default {
        components: {
            VuePerfectScrollbar,
            chart1,
        },
        name: "StrategySimulator",
        data(){
            return{
                stockNum:[],
                date:'',
                budget:'',
                stockCode:[],
                stockList:[],
                ratio:[],
                tmp:0

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
                        this.$http.get('/test/:'+this.date).then(response=>{
                            console.log(response.data[0],response.data[1]);
                            this.stockList=response.data;
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
                    a += this.ratio[i]
                }
                if(a!=100){
                    alert('비중의 총합이 100이 되도록 재설정하세요.')
                    return false
                }
                else{
                    //validation하고 맞으면 입력받은 date랑 stockCode를 back으로 보내

                }
            },
            datechangeInit: function () {
                this.stockNum.splice(0,this.stockNum.length);
                this.stockList.splice(0,this.stockList.length);
                this.stockCode.splice(0,this.stockCode.length);
                this.ratio.splice(0,this.ratio.length);
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