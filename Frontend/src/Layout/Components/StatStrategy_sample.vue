<template>
    <div id="StatStrategy">
        <div id="selectZone">
                <div id="strategy">
                    <div id="textZone">
                        <h2>블루칩</h2>
                        <p>
                            <strong>"안정적인 우량주에 투자하세요"</strong><br><br>
                            시가총액 5천억원 이상이며 거래량이 풍부한 안전한 종목 위주로 선택합니다. 
                            가격 리스크가 적은 대형주와 수익성과 성장성 측면에서 우수한 우량주 위주로 보유합니다. 
                            다만 최근 수익률이 너무 저조하면 제외합니다. 블루칩은 대형주 위주의 포트폴리오기 때문에 시장과 상관계수가 매우 높습니다. 
                            주식시장의 리더들을 모아 놓은 것이기 때문에 장기적으로 보면 시장을 이길 수 있습니다.<br><br>
                        </p>
                        <ul>
                            <li>사이즈 스코어 5 이상</li>
                            <li>수익성 스코어 3 이상</li>
                            <li>거래량 스코어 4 이상</li>
                        </ul>
                        <b-button variant="outline-info" class="graphBtn"  @click="showRadar(1)">그래프 보기</b-button>
                    </div>
                    <div id="graphZone">
                        <canvas id="radar1" width="450" height="300"></canvas>
                    </div>
                </div>

                <div id="strategy">
                    <div id="textZone">
                        <h2>대형성장</h2>
                        <p>
                            <strong>"성장 여력이 높은 대형주에 투자하세요"</strong><br><br>
                            시가총액 5천억원 이상 대형주 중에서 성장성이 높거나 실적이 턴어라운드 
                            된 종목 위주로 선택하여 기업의 펀더멘탈 모멘텀에 투자합니다. 
                            대형성장은 현재 주가 자체가 고평가 되어 있을지도 모르나 중장기적으로 추가적인 수익률을 추구합니다.<br><br>
                        </p>
                        <ul>
                            <li>사이즈 스코어 5 이상</li>
                            <li>성장성 스코어 4 이상</li>
                            <li>거래량 스코어 3 이상</li>
                            <li>모멘텀 스코어 2 이상 4 이하</li>
                        </ul>
                        <b-button variant="outline-info" class="graphBtn"  @click="showRadar(2)">그래프 보기</b-button>
                    </div>
                    <div id="graphZone"><canvas id="radar2" width="450" height="300"></canvas></div>
                </div>
                
                <div id="strategy">
                    <div id="textZone">
                        <h2>중소형밸류</h2>
                        <p>
                            <strong>"작은 종목이지만 아직 정당한 평가를 받지 못한 종목에 투자하세요"</strong><br><br>
                            사이즈(시가총액)이 작지만 저평가 되어 있는 종목 위주로 고릅니다. 
                            성장성과 수익성과 같은 <br>펀더멘탈 역시 
                            우수하지만 현재 하락한 주가로 인하여 미래 상승여력이 충분한 종목을 선택합니다.<br><br>
                        </p>
                        <ul>
                            <li>사이즈 스코어 2 이상 3 이하</li>
                            <li>저평가 스코어 5 이상</li>
                            <li>수익성 스코어 4 이상</li>
                            <li>성장성 스코어 4 이상</li>
                        </ul>
                        <b-button variant="outline-info" class="graphBtn"  @click="showRadar(3)">그래프 보기</b-button>
                    </div>

                    <div id="graphZone"><canvas id="radar3" width="450" height="300"></canvas></div>
                </div>
                
                <div id="strategy">
                    <div id="textZone">
                        <h2>컨트래리안</h2>
                        <p>
                            <strong>"반등을 노려보세요"</strong><br><br>
                            컨트래리안 전략이란, 비록 최근에 주가가 크게 하락했지만 
                            기업의 내재가치는 괜찮은 종목들을 선택하여 향후 반등을 노리는 전략입니다. 
                            위험이 큰 전략이지만 그만큼 큰 수익을 얻을 수 있습니다.<br><br>
                        </p>
                        <ul>
                            <li>거래량 스코어 3 이상 5 이하</li>
                            <li>모멘텀 1 이하</li>
                            <li>성장성 스코어 3 이상</li>
                            <li>수익성 스코어 4 이상</li>
                        </ul>
                        <b-button variant="outline-info" class="graphBtn"  @click="showRadar(4)">그래프 보기</b-button>
                    </div>
                    <div id="graphZone"><canvas id="radar4" width="450" height="300"></canvas></div>
                </div>
                
                <div id="strategy">
                    <div id="textZone">
                        <h2>로우볼</h2>
                        <p>
                            <strong>"저변동성 팩터에 투자하세요"</strong><br><br>
                            2014년도에 가장 뜨거웠던 스마트베타가 '로우볼'이라는 사실을 아시나요? 
                            학술적으로는 '하이리스크 하이리턴' 이란 말이 있습니다. 
                            즉, 변동성이 높을 수록 높은 기대 수익율을 얻고 반대로 낮은 변동성은 낮은 기대수익률을 의미합니다. 
                            다만 글로벌 시장 전체적으로 저변동성을 갖는 종목이 높은 수익률을 보이는 이상현상이 존재합니다. 
                            로우볼 포트폴리오는 이를 위하여 낮은 변동성을 가진 종목을 종목을 선택합니다.<br><br>
                        </p>
                        <ul>
                            <li>사이즈 스코어 2 이상 5 이하</li>
                            <li>거래량 스코어 2 이상</li>
                            <li>저평가 스코어 2 이상</li>
                        </ul>
                        <b-button variant="outline-info" class="graphBtn"  @click="showRadar(5)">그래프 보기</b-button>
                    </div>
                    <div id="graphZone"><canvas id="radar5" width="450" height="300"></canvas></div>
                </div>
                

        </div>
    </div>
           
</template>

<script>
    import Chart from 'chart.js'

    export default {
        name: "StatStrategy_sample",
        data(){
            return{
                MinStat:[3,3,2,2,2,2],
                MaxStat:[4,5,4,4,4,4],
                StatInfo:[],
                date:''
            }
        },
        methods:{
            StatAdjust: function (i,adj) {
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
            calculateRadar:function (i) {
                var ctx = document.getElementById("radar"+i);
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
            showRadar:function (i) {
                if(i==1){                       //블루칩전략
                    //사이즈 스코어5이상
                    this.MinStat[0]=5
                    this.MaxStat[0]=5
                    //수익성 스코어3이상
                    this.MinStat[5]=3
                    this.MaxStat[5]=5
                    //거래량 스코어4이상
                    this.MinStat[1]=4
                    this.MaxStat[1]=5
                }
                else if(i==2){                  //대형성장전략
                    //사이즈 스코어5이상
                    this.MinStat[0]=5
                    this.MaxStat[0]=5
                    //성장성 스코어 4이상
                    this.MinStat[4]=4
                    this.MaxStat[4]=5
                    //거래량 스코어3이상
                    this.MinStat[1]=3
                    this.MaxStat[1]=5
                    //모멘텀 스코어 2이상 4이하
                    this.MinStat[2]=2
                    this.MaxStat[2]=4
                }
                else if(i==3){                  //중소형밸류전략
                    //사이즈 스코어 2 이상 3 이하
                    this.MinStat[0]=2
                    this.MaxStat[0]=3
                    //저평가 스코어 5 이상
                    this.MinStat[3]=5
                    this.MaxStat[3]=5
                    //수익성 스코어 4 이상
                    this.MinStat[5]=4
                    this.MaxStat[5]=5
                    //성장성 스코어 4 이상
                    this.MinStat[4]=4
                    this.MaxStat[4]=5
                }
                else if(i==4){                  //컨트래리안전략
                    //거래량 스코어 3 이상 5 이하
                    this.MinStat[1]=3
                    this.MaxStat[1]=5
                    //모멘텀 1 이하
                    this.MinStat[2]=1
                    this.MaxStat[2]=1
                    //성장성 스코어 3 이상
                    this.MinStat[4]=3
                    this.MaxStat[4]=5
                    //수익성 스코어 4 이상
                    this.MinStat[5]=4
                    this.MaxStat[5]=5
                }
                else if(i==5){                  //로우볼전략
                    //사이즈 스코어 2 이상 5 이하
                    this.MinStat[0]=2
                    this.MaxStat[0]=5
                    //거래량 스코어 2 이상
                    this.MinStat[1]=2
                    this.MaxStat[1]=5
                    //저평가 스코어 2 이상
                    this.MinStat[3]=2
                    this.MaxStat[3]=5
                }
                //this.chartOn=true
                document.getElementById('graphZone').style.display="";
                this.calculateRadar(i)
            },
            hideRadar: function () {
                this.chartOn=false;
                document.getElementById('graphZone').style.display="none"
            },
            showRecommend: function () {
                this.$router.push('/pages/Recommend');
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
#textZone{
    width: 50%;
    float: left;
}
#strategy{
    border-bottom: 1px solid black;
    height: 360px;
}
#graphZone{
    width: 45%;
    height: 350px;
    float: right;
}
#resultTable{
    width: 95%;
    text-align: center;
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