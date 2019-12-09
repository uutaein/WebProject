<template>
    <div id="StatStrategy">
        <div id="selectZone">
            <h1>
                주식스탯전략 시뮬레이터<br>
            </h1>
            <p>주식스탯으로 세워보는 나만의 전략(2018.12 기준)</p><hr>
            <div id="graphzone" style="display: none">
                <canvas id="Radar" width="450" height="300"></canvas>
            </div>
            <b-button variant="outline-info" class="graphBtn" v-if="!chartOn" @click="showRadar">그래프 보기</b-button>
            <b-button variant="outline-info" class="graphBtn" v-if="chartOn" @click="hideRadar">그래프 숨기기</b-button>
            <div>
                <span class="statBtnContainer">
                    <b-button variant="info" class="pe-7s-angle-left-circle" @click="MinStatAdjust(0,0)"></b-button>
                    <b-button variant="info" class="pe-7s-angle-right-circle" @click="MinStatAdjust(0,1)"></b-button>
                    <span class="statName">사이즈</span>
                    <b-button class="helpBtn" variant="outline-dark" size="sm" @click="popupInfo(0)">?</b-button>
                    <b-button variant="danger" class="pe-7s-angle-left-circle" @click="MaxStatAdjust(0,0)"></b-button>
                    <b-button variant="danger" class="pe-7s-angle-right-circle" @click="MaxStatAdjust(0,1)"></b-button>
                    <span id="scope0">{{MinStat[0]}} ~ {{MaxStat[0]}}</span>
                </span><br><br>
                <span class="statBtnContainer">
                    <b-button variant="info" class="pe-7s-angle-left-circle" @click="MinStatAdjust(1,0)"></b-button>
                    <b-button variant="info" class="pe-7s-angle-right-circle" @click="MinStatAdjust(1,1)"></b-button>
                    <span class="statName">거래량</span>
                    <b-button class="helpBtn" variant="outline-dark" size="sm" @click="popupInfo(1)">?</b-button>
                    <b-button variant="danger" class="pe-7s-angle-left-circle" @click="MaxStatAdjust(1,0)"></b-button>
                    <b-button variant="danger" class="pe-7s-angle-right-circle" @click="MaxStatAdjust(1,1)"></b-button>
                    <span id="scope1">{{MinStat[1]}} ~ {{MaxStat[1]}}</span>
                </span><br><br>
                <span class="statBtnContainer">
                    <b-button variant="info" class="pe-7s-angle-left-circle" @click="MinStatAdjust(2,0)"></b-button>
                    <b-button variant="info" class="pe-7s-angle-right-circle" @click="MinStatAdjust(2,1)"></b-button>
                    <span class="statName">모멘텀</span>
                    <b-button class="helpBtn" variant="outline-dark" size="sm" @click="popupInfo(2)">?</b-button>
                    <b-button variant="danger" class="pe-7s-angle-left-circle" @click="MaxStatAdjust(2,0)"></b-button>
                    <b-button variant="danger" class="pe-7s-angle-right-circle" @click="MaxStatAdjust(2,1)"></b-button>
                    <span id="scope2">{{MinStat[2]}} ~ {{MaxStat[2]}}</span>
                </span><br><br>
                <span class="statBtnContainer">
                    <b-button variant="info" class="pe-7s-angle-left-circle" @click="MinStatAdjust(3,0)"></b-button>
                    <b-button variant="info" class="pe-7s-angle-right-circle" @click="MinStatAdjust(3,1)"></b-button>
                    <span class="statName">저평가</span>
                    <b-button class="helpBtn" variant="outline-dark" size="sm" @click="popupInfo(3)">?</b-button>
                    <b-button variant="danger" class="pe-7s-angle-left-circle" @click="MaxStatAdjust(3,0)"></b-button>
                    <b-button variant="danger" class="pe-7s-angle-right-circle" @click="MaxStatAdjust(3,1)"></b-button>
                    <span id="scope3">{{MinStat[3]}} ~ {{MaxStat[3]}}</span>
                </span><br><br>
                <span class="statBtnContainer">
                    <b-button variant="info" class="pe-7s-angle-left-circle" @click="MinStatAdjust(4,0)"></b-button>
                    <b-button variant="info" class="pe-7s-angle-right-circle" @click="MinStatAdjust(4,1)"></b-button>
                    <span class="statName">성장성</span>
                    <b-button class="helpBtn" variant="outline-dark" size="sm" @click="popupInfo(4)">?</b-button>
                    <b-button variant="danger" class="pe-7s-angle-left-circle" @click="MaxStatAdjust(4,0)"></b-button>
                    <b-button variant="danger" class="pe-7s-angle-right-circle" @click="MaxStatAdjust(4,1)"></b-button>
                    <span id="scope4">{{MinStat[4]}} ~ {{MaxStat[4]}}</span>
                </span><br><br>
                <span class="statBtnContainer">
                    <b-button variant="info" class="pe-7s-angle-left-circle" @click="MinStatAdjust(5,0)"></b-button>
                    <b-button variant="info" class="pe-7s-angle-right-circle" @click="MinStatAdjust(5,1)"></b-button>
                    <span class="statName">수익성</span>
                    <b-button class="helpBtn" variant="outline-dark" size="sm" @click="popupInfo(5)">?</b-button>
                    <b-button variant="danger" class="pe-7s-angle-left-circle" @click="MaxStatAdjust(5,0)"></b-button>
                    <b-button variant="danger" class="pe-7s-angle-right-circle" @click="MaxStatAdjust(5,1)"></b-button>
                    <span id="scope5">{{MinStat[5]}} ~ {{MaxStat[5]}}</span>
                </span>
            </div>
            <b-button variant="primary" id="findStockBtn" @click="findCompany">종목 찾기</b-button>
            <b-button variant="focus" id="recommendBtn" @click="showRecommend">추천 전략 보기</b-button>
            <b-button variant="warning" id="rankManualBtn" @click="rankManualPopup">점수 산정기준</b-button>
        </div>
        <div id="tableZone" v-if="tableOn">
            <table id="resultTable" border="1" bordercolor="#3ac18a">
                <tr bgcolor="#3AC18A" style="color: white">
                    <td width="180px">종목명</td>
                    <td width="120px">시가총액<br>(단위:억원)</td>
                    <td>PER(배)</td>
                    <td width="140px">영업이익(%)</td>
                    <td>ROE(%)</td>
                    <td width="100px">3개월<br>수익률</td>
                </tr>
                <tr v-for="idx in filteredStockData" v-bind:value="idx.name">
                    <td>{{idx.name}}</td>
                    <td>{{idx.stock_capital}}</td>
                    <td>{{idx.per}}</td>
                    <td>{{idx.net_profit}}</td>
                    <td>{{idx.roe}}</td>
                    <td>{{idx.profit_3m}}</td>
                </tr>
            </table>
        </div>
    </div>
</template>

<script>
    import Chart from 'chart.js'

    export default {
        name: "StatStrategy",
        data(){
            return{
                MinStat:[3,3,2,2,2,2],
                MaxStat:[4,5,4,4,4,4],
                StatInfo:[],
                date:'',
                chart:'',
                chartOn:false,
                tableOn:false,
                filteredStockData:[{name:'삼성',total:'300조 8,770억',variability:'10%',PER:6.42,profit:24.16,ROE:19.63},
                    {name:'애플',total:'300조 8,770억',variability:'10%',PER:6.42,profit:24.16,ROE:19.63},]
            }
        },
        methods:{
            StatInfoInit:function(){
                var sizeInfo='사이즈는 주식에 있어서 빠질 수 없는 요소입니다.\n ' +
                    '기업 규모에 따라서 시장에 미치는 영향이 다르기 때문입니다. 또한 국내 대표적 벤치마크의 대상인 KOSPI 시가총액 가중방식이 때문에 시장을 어느 수준 따라고 싶다면 대형주를 많이 보유하는 것이 좋습니다'
                this.StatInfo.push(sizeInfo);
                var volumeInfo='거래량은 주식에 있어서 매우 중요한 요소 입니다.\n ' +
                    '아무리 좋은 종목이라도, 주문을 내서 체결될 수 없는 종목이라면 의미가 없기 때문입니다. 거래량이 작을 경우 대량 매수 주문을 낼 경우 손해를 입을 수 있습니다. 만약 운용중인 펀드의 규모가 크다면 거래량을 반드시 고려하는 것이 좋습니다.'
                this.StatInfo.push(volumeInfo);
                var momentumInfo='주가에는 랠리와 반등구간이 있습니다. 모멘텀 스탯은 최근에 얼마나 올랐느냐에 대한 지표입니다.\n ' +
                    '만약 선택한 종목이 추가적인 상승 모멘텀이 있다고 판단되면 최근에 오른 종목을 고르는 것이 좋습니다. 또한 반등을 노리는 컨트래리안 전략을 사용한다면 최근에 하락한 종목을 선택하는 것이 좋습니다.'
                this.StatInfo.push(momentumInfo);
                var assessInfo='기업의 내재가치에 비하여 현재 주가가 어떻게 형성되어 있는가를 봅니다.\n ' +
                    '만약 기업의 내재가치에 비하여 최근 주가가 높다면 이는 고평가 되어 있다는 뜻이고, 내재가치에 비하여 최근 주가가 낮다면 기업이 저평가 되어 있다는 뜻입니다. 이를 판단하기 위하여 투자지표인 PER을 사용합니다. 다만 PER을 전체 주식에 대하여 동일한 기준으로 적용하는 것은 무리가 있습니다. 똑같은 PER 10이라도 제조업과 은행업의 그것은 다른 의미이기 때문입니다. 따라서 동일한 업종 내의 상대적인 값을 사용합니다.'
                this.StatInfo.push(assessInfo);
                var potentInfo='장기투자를 목적으로 한다면 당연히 기업의 성장성을 염두하셔야 합니다.\n ' +
                    '주가란 기업의 미래가치에 대한 현재의 기대이기 때문입니다. 지난해에 비해 올해 매출액이나 영업이익이 큰 폭으로 성장한 기업이라면 당연히 주가 역시 상승할 종목입니다. 다만 성장성 스코어는 최근 결산 기준의 재무데이터를 사용하기 때문에 주가에 대부분 선반영 되어 있습니다. 따라서 장기 투자 시에 고려해야 할 요소입니다. 성장성은 업종마다 특이성이 존재하기 때문에 동일업종 내의 상대적인 값을 사용합니다.'
                this.StatInfo.push(potentInfo);
                var profitInfo='주가란 결국 그 기업이 앞으로 얻게 될 현금들의 현재 시점의 기대값입니다.\n ' +
                    '그럼 이 종목이 얼마나 돈을 잘 버는 기업인지를 판단하는 것이 중요하겠지요. 투자한 금액 대비 기업이 얼마나 많은 이익을 창출하고 있는지를 확인하기 위하여 ROE, ROI 와 같은 투자지표를 사용합니다. ROE는 업종마다 특이성이 존재하기 때문에, 수익성을 판단하기 위해 동일업종 내의 상대적인 값을 사용합니다.'
                this.StatInfo.push(profitInfo);
            },
            popupInfo:function (i) {
                if(this.StatInfo.length==0) this.StatInfoInit();
                alert(this.StatInfo[i]);
            },
            rankManualPopup:function () {
                var rankInfo='Score 5 : 해당스탯 상위 20% 이내\n' +
                    'Score 4 : 해당스탯 상위 40% 이내\n' +
                    'Score 3 : 해당스탯 상위 60% 이내\n' +
                    'Score 2 : 해당스탯 상위 80% 이내\n' +
                    'Score 1 : 그 외'
                alert(rankInfo);
            },
            MinStatAdjust: function (i,adj) {
                //Minstat의 i번째 값이 adj가 1이면 증가 0이면 감소
                if(adj==1){
                    if(this.MaxStat[i]==this.MinStat[i]) {
                        alert('Min값은 Max값보다 커질 수 없습니다.')
                        return;
                    }
                    this.MinStat[i]++;
                    if(this.MinStat[i]>5) this.MinStat[i]=5;
                    this.calculateRadar()
                }
                else if(adj==0){
                    if(this.MinStat[i]==0) return
                    this.MinStat[i]--;
                    this.calculateRadar()
                }
                var scope;
                if(this.MinStat[i]==this.MaxStat[i]) scope=this.MinStat[i]
                else scope=this.MinStat[i]+ '~' +this.MaxStat[i]
                document.getElementById('scope'+i).innerHTML=scope
            },
            MaxStatAdjust: function (i,adj) {
                //Maxstat의 i번째 값이 adj가 1이면 증가 0이면 감소
                if(adj==1){
                    this.MaxStat[i]++;
                    if(this.MaxStat[i]>5) this.MaxStat[i]=5;
                    this.calculateRadar()
                }
                else if(adj==0){
                    if(this.MinStat[i]==this.MaxStat[i]){
                        alert('Max값은 Min값보다 작아질 수 없습니다.')
                        return;
                    }
                    if(this.MaxStat[i]==0) return
                    this.MaxStat[i]--;
                    this.calculateRadar()
                }
                var scope;
                if(this.MinStat[i]==this.MaxStat[i]) scope=this.MinStat[i]
                else scope=this.MinStat[i]+ '~' +this.MaxStat[i]
                document.getElementById('scope'+i).innerHTML=scope
            },
            calculateRadar:function () {
                var ctx = document.getElementById("Radar");
                let radar = new Chart(ctx, {
                    type: 'radar',
                    data: {
                        labels: ['사이즈', '거래량', '모멘텀', '저평가', '성장성', '수익성'],
                        datasets: [
                            {
                                label: 'Min',
                                backgroundColor: 'rgba(00,181,198,0.2)',
                                borderColor: '#6CC3D5',
                                pointBackgroundColor: '#6CC3D5',
                                pointBorderColor: '#fff',
                                data: this.MinStat
                            },
                            {
                                label: 'Max',
                                backgroundColor: 'rgba(255,99,132,0.2)',
                                borderColor: '#FF7851',
                                pointBackgroundColor: '#FF7851',
                                pointBorderColor: '#fff',
                                data: this.MaxStat
                            }
                        ]
                    },
                    options: {
                        tooltips:false,
                        hover:false,
                        scale:{
                            ticks:{
                                min:0,
                                max:5,
                                stepSize:1
                            }
                        },
                        responsive: false
                    }
                })
            },
            showRadar:function () {
                this.chartOn=true
                document.getElementById('graphzone').style.display=""
                this.calculateRadar()
            },
            hideRadar: function () {
                this.chartOn=false;
                document.getElementById('graphzone').style.display="none"
            },
            showRecommend: function () {
                this.$router.push('/pages/Recommend');
            },
            findCompany: function(){
                this.tableOn=true;
                this.clearTable();
                this.$http.post('/test/stat',{minstat : this.MinStat , maxstat: this.MaxStat}).then(response=>{
                    console.log(response.data);
                    /*  data(){
                                return{
                                    MinStat:[1,1,1,1,1,1],
                                    MaxStat:[2,2,2,2,2,2],
                                    StatInfo:[],
                                    date:'',
                                    chart:'',
                                    chartOn:false,
                                    tableOn:false,
                                    filteredStockData:[{name:'삼성',total:'300조 8,770억',variability:'10%',PER:6.42,profit:24.16,ROE:19.63},
                                        {name:'애플',total:'300조 8,770억',variability:'10%',PER:6.42,profit:24.16,ROE:19.63},]
                                }
                        } 
                        this.stockList=response.data;
                    */
                   this.filteredStockData = response.data;
                })
            },
            clearTable: function () {
                var tb=document.getElementById('resultTable');
                if(tb!=null){
                    while(tb.childElementCount>1){
                        tb.removeChild(tb.lastChild);
                    }
                }
            }
        }
    }
</script>

<style scoped>
#selectZone{
    width: 50%;
    float: left;
}
#tableZone{
    width: 45%;
    float: right;
}
#resultTable{
    width: 95%;
    text-align: center;
}
#graphzone{
    height: 350px;
}
.graphBtn{
    width: 24%;
}
#findStockBtn{
    width: 24%;
}
#rankManualBtn{
    width:24%;
}
#recommendBtn{
    width: 24%;
}
.helpBtn{
    width: 5%;
}
.statName{
    width: 5%;
    margin: 5px;
}
button{
    width: 14%;
}


</style>