<template>
    <div>
        <div class="main-card mb-3 card" v-if="!init_state_done">
            <div class="card-body">
                <h2 class="card-title">모의 주식투자</h2>
                <form class="">
                    <div class="form-row">
                        <div class="col-md-6">
                            <div class="position-relative form-group">
                                <label for="startdate" class="">시작날짜</label
                                ><input
                                    v-model="start_date"
                                    placeholder="시작날짜를 정해주세요"
                                    type="date"
                                    class="form-control"
                                />
                            </div>
                        </div>
                        <div class="col-md-6">
                            <div class="position-relative form-group">
                                <label for="examplePassword11" class=""
                                    >시작금액(단위 : 만 원)</label
                                ><input
                                    v-model="init_money"
                                    placeholder="시작금액을 정해주세요"
                                    type="number"
                                    class="form-control"
                                />
                            </div>
                        </div>
                    </div>
                    <div class="text-center d-block p-3 card-footer">
                        <button
                            class="btn-pill btn-shadow btn-wide fsize-1 btn btn-primary btn-lg"
                            @click="set_init_state"
                        >
                            <span class="mr-2 opacity-7">
                                <i
                                    class="icon icon-anim-pulse ion-ios-analytics-outline"
                                ></i>
                            </span>
                            <span class="mr-1">모의투자 시작하기</span>
                        </button>
                    </div>
                </form>
            </div>
        </div>
        <!--위에 입력 테이블 끝 -->
        <!--왼쪽 테이블 시작-->
        <div class="row">
            <div class="col-sm-12 col-lg-6">
                <div class="mb-3 card">
                    <div class="card-header-tab card-header">
                        <div
                            class="card-header-title font-size-lg text-capitalize font-weight-normal"
                        >
                            <i
                                class="header-icon lnr-cloud-download icon-gradient bg-happy-itmeo"
                            >
                            </i>
                            주식 목록

                            <b-button
                                class="btn-pill btn-shadow btn-wide fsize-1 btn btn-primary btn-lg"
                                variant="success"
                                style="float : right"
                                @click="addStock"
                                size="lg"
                                >종목추가</b-button
                            >
                        </div>
                    </div>
                    <div class="main-card mb-3 card">
                        <div class="card-body">
                            <div v-for="(idx, i) in stockNum" class="row">
                                {{ passer(i) }}
                                <div class="position-relative form-group">
                                    <select
                                        id="stockCode"
                                        v-model="stockCode[i]"
                                        class="custom-select"
                                    >
                                        <option
                                            v-for="idx in stockList"
                                            v-bind:value="idx.code"
                                            >종목코드:{{ idx.code }} 종목명:{{
                                                idx.name
                                            }}
                                        </option>
                                    </select>
                                </div>
                                <div class="position-relative form-group">
                                    <input
                                        v-model="ratio[i]"
                                        type="number"
                                        placeholder="비중(%)"
                                        class="form-control"
                                    />
                                </div>
                                <div class="position-relative form-group">
                                    <b-button
                                        class="btn-pill btn-shadow btn-wide fsize-1 btn btn-primary btn-sm"
                                        variant="warning"
                                        style="float : right; margin-left : 20px"
                                        @click="deleteStock"
                                        size="lg"
                                        >종목삭제</b-button
                                    >
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="text-center d-block mb-3 card-footer">
                        <button
                            class="btn-pill btn-shadow btn-wide fsize-1 btn btn-primary btn-lg"
                            @click="validation"
                            v-if="stockCode.length != 0 && !portfolio_done"
                            style="margin : 20px"
                        >
                            <span class="mr-2 opacity-7">
                                <i
                                    class="icon icon-anim-pulse ion-ios-analytics-outline"
                                ></i>
                            </span>
                            <span class="mr-1">포트폴리오 구성</span>
                        </button>
                        <button
                            class="btn-pill btn-shadow btn-wide fsize-1 btn btn-primary btn-lg"
                            @click="portfolio_init(3)"
                            v-if="portfolio_done"
                            style="margin : 20px"
                        >
                            <span class="mr-2 opacity-7">
                                <i
                                    class="icon icon-anim-pulse ion-ios-analytics-outline"
                                ></i>
                            </span>
                            <span class="mr-1">3개월 투자하기</span>
                        </button>

                        <button
                            class="btn-pill btn-shadow btn-wide fsize-1 btn btn-primary btn-lg"
                            @click="portfolio_init(6)"
                            v-if="portfolio_done"
                            style="margin : 20px"
                        >
                            <span class="mr-2 opacity-7">
                                <i
                                    class="icon icon-anim-pulse ion-ios-analytics-outline"
                                ></i>
                            </span>
                            <span class="mr-1">6개월 투자하기</span>
                        </button>

                        <button
                            class="btn-pill btn-shadow btn-wide fsize-1 btn btn-primary btn-lg"
                            @click="portfolio_init(12)"
                            v-if="portfolio_done"
                            style="margin : 20px"
                        >
                            <span class="mr-2 opacity-7">
                                <i
                                    class="icon icon-anim-pulse ion-ios-analytics-outline"
                                ></i>
                            </span>
                            <span class="mr-1">1년 투자하기</span>
                        </button>
                    </div>
                </div>
            </div>
            <!--왼쪽 테이블 끝-->
            <!--오른쪽 차트 시작-->
            <div class="col-sm-12 col-lg-6">
                <div class="mb-3 card">
                    <div class="card-header-tab card-header">
                        <div
                            class="card-header-title font-size-lg text-capitalize font-weight-normal"
                        >
                            <i
                                class="header-icon lnr-cloud-download icon-gradient bg-happy-itmeo"
                            >
                            </i>
                            포트폴리오 변동 그래프
                        </div>
                    </div>
                    <div class="p-0 card-body">
                        <b-card class="mb-3 nav-justified" no-body>
                            <b-tabs pills card>
                                <b-tab title="현재 구간 수익률" active>
                                    <div class="p-1 slick-slider-sm mx-auto">
                                        <div
                                            class="widget-chart widget-chart2 text-left p-0"
                                        >
                                            <div
                                                class="widget-chat-wrapper-outer"
                                            >
                                                <div
                                                    class="widget-chart-content widget-chart-content-lg pb-0"
                                                >
                                                    <div
                                                        class="widget-chart-flex"
                                                    >
                                                        <div
                                                            class="widget-title opacity-5 text-muted text-uppercase"
                                                        >
                                                            Helpdesk Tickets
                                                        </div>
                                                    </div>
                                                    <div class="widget-numbers">
                                                        <div
                                                            class="widget-chart-flex"
                                                        >
                                                            <div>
                                                                <span
                                                                    class="text-warning"
                                                                    >34</span
                                                                >
                                                            </div>
                                                            <div
                                                                class="widget-title ml-2 font-size-lg font-weight-normal text-dark"
                                                            >
                                                                <span
                                                                    class="opacity-5 text-muted pl-2 pr-1"
                                                                    >5%</span
                                                                >
                                                                increase
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                                <div
                                                    class="widget-chart-wrapper he-auto opacity-10 m-0"
                                                >
                                                    <IGchart :height="145" v-if="this.$store.state.IG_chart_done"/>
                                                </div>
                                            </div>
                                        </div>
                                    </div>

                                    <h6
                                        class="text-muted text-uppercase font-size-md opacity-5 pl-3 pr-3 pb-1 font-weight-normal"
                                    >
                                        Sales Progress
                                    </h6>
                                    <ul class="list-group list-group-flush">
                                        <li
                                            class="p-3 bg-transparent list-group-item"
                                        >
                                            <div class="widget-content p-0">
                                                <div
                                                    class="widget-content-outer"
                                                >
                                                    <div
                                                        class="widget-content-wrapper"
                                                    >
                                                        <div
                                                            class="widget-content-left"
                                                        >
                                                            <div
                                                                class="widget-heading"
                                                            >
                                                                Total Orders
                                                            </div>
                                                            <div
                                                                class="widget-subheading"
                                                            >
                                                                Last year
                                                                expenses
                                                            </div>
                                                        </div>
                                                        <div
                                                            class="widget-content-right"
                                                        >
                                                            <div
                                                                class="widget-numbers text-success"
                                                            >
                                                                <small>$</small>
                                                                1896
                                                            </div>
                                                        </div>
                                                    </div>
                                                    <div
                                                        class="widget-progress-wrapper"
                                                    >
                                                        <div
                                                            class="progress-bar-sm progress-bar-animated-alt progress"
                                                        >
                                                            <div
                                                                class="progress-bar bg-primary"
                                                                role="progressbar"
                                                                aria-valuenow="43"
                                                                aria-valuemin="0"
                                                                aria-valuemax="100"
                                                                style="width: 43%;"
                                                            ></div>
                                                        </div>
                                                        <div
                                                            class="progress-sub-label"
                                                        >
                                                            <div
                                                                class="sub-label-left"
                                                            >
                                                                YoY Growth
                                                            </div>
                                                            <div
                                                                class="sub-label-right"
                                                            >
                                                                100%
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </li>
                                    </ul>
                                </b-tab>
                                <b-tab title="누적 수익률"> </b-tab>
                            </b-tabs>
                        </b-card>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import IGchart from './Analytics/IG_chart1';
import VuePerfectScrollbar from 'vue-perfect-scrollbar';

export default {
    
     components: {
            VuePerfectScrollbar,
            IGchart,
    },
    name: "InvestmentGame",
    data() {
        return {
            stockNum: [],
            stockCode: [],
            start_date: "",
            tstart_date : "",
            tend_date : "",
            end_date : "2019-11-26",
            init_money: this.$store.state.IG_init_money,
            init_state_done: false,
            stockList: [],
            ratio: this.$store.state.IG_ratio,
            portfolio_done: false,
        };
    },
    methods: {
        set_init_state: function() {
            if (this.init_money != 0 && this.start_date != "") {
                this.init_money *= 10000;
                this.$store.state.IG_init_money = this.init_money;
                this.$store.state.IG_init_date = this.date;
                this.init_state_done = true;
            } else {
                alert("입력을 확인해주세요");
            }
        },
        addStock: function() {
            if (this.init_state_done == false) {
                alert("값을 입력해주세요");
                return;
            } else {
                this.stockNum.push(null);
                if (this.stockList.length == 0) {
                    console.log(this.start_date);
                    this.$http.get("/test/" + this.date).then(response => {
                        this.stockList = response.data;
                    });
                }
            }
        },
        passer: function(i) {
            this.tmp = i;
        },
        deleteStock: function() {
            //종목삭제할때 input값 초기화할때 쓰는 함수
            this.ratio[this.tmp] = "";
            this.stockNum.pop();
        },
        validation: function() {
            //입력완료 눌렀을때 비중입력 총합 100이하인지 확인하는 함수
            var a = 0;
            for (var i = 0; i < this.ratio.length; i++) {
                a += Number(this.ratio[i]);
            }
            if (a != 100) {
                alert("비중의 총합이 100이 되도록 재설정하세요.");
                return false;
            } else {
                this.portfolio_done = true;
                console.log(this.stockCode);
                //this.portfolio_init();
                // this.$store.dispatch("calculatePortfolio", {
                //     date: this.date,
                //     stockCode: this.stockCode,
                //     ratio: this.ratio
                // });
                //validation하고 맞으면 입력받은 date랑 stockCode를 back으로 보내
            }
        },
        portfolio_init: function(month) {
            
            if(this.tstart_date == "")
            {
                var tdatetime;
                this.tstart_date = this.start_date;
                tdatetime = this.parse_string_to_date(this.tstart_date);
                tdatetime.setMonth(tdatetime.getMonth() + month);
                this.tend_date = this.date_to_string(tdatetime);
            }
            else
            {
                var tdatetime;
                this.tstart_date = this.tend_date;
                tdatetime = this.parse_string_to_date(this.tstart_date);
                tdatetime.setMonth(tdatetime.getMonth() + month);
                this.tend_date = this.date_to_string(tdatetime);
            }
            this.$store.dispatch("IGcalculatePortfolio",{
                    start_date : this.tstart_date,
                    end_date : this.tend_date,
                    stockCode : this.stockCode,
                    ratio : this.ratio, 
            });
        },
        parse_string_to_date : function(str)
        {
            var y = str.substr(0,4),
                    m = str.substr(5,2)-1,
                    d = str.substr(8,2);
            return new Date(y,m,d);
        },
        date_to_string : function(date)
        {
            console.log("date_string:" + date);
            var y = String(date.getFullYear())
            var m = String(date.getMonth()+1)
            var d = String(date.getDate())
            if(d.length == 1) d= '0'+d;
            if(m.length ==1) m = '0' + m;
            var  dateString = y +'-'+  m +'-' +d;
            return dateString;
        },
    }
};
</script>
