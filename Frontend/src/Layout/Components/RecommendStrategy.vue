<template>
    <div id="RecommendStrategy">
        <div id="line1" class="line">
            <div class="graphZone">
                <canvas id="g1" width="300" height="300"></canvas>
            </div>
            <div class="descriptionZone">
                <p class="descName">블루칩</p>
                <span><strong>안정적인 우량주에 투자하기</strong></span>
                <p>시가총액 5천억원 이상이며 거래량이 풍부한 안전한 종목 위주로 선택합니다. 가격 리스크가 적은 대형주와 수익성과 성장성 측면에서 우수한 우량주 위주로 보유합니다. 다만 최근 수익률이 너무 저조하면 제외합니다. 블루칩은 대형주 위주의 포트폴리오기 때문에 시장과 상관계수가 매우 높습니다. 주식시장의 리더들을 모아 놓은 것이기 때문에 장기적으로 보면 시장을 이길 수 있습니다.</p>
                <ul>
                    <li>사이즈 score 5이상</li>
                    <li>수익성 score 3이상</li>
                    <li>거래량 score 4이상</li>
                </ul>
            </div>
        </div>
        <div id="line2" class="line">
            <div class="graphZone">
                <canvas id="g2" width="300" height="300"></canvas>
            </div>
            <div class="descriptionZone">
                <p class="descName">대형성장</p>
                <span><strong>성장 여력이 높은 대형주에 투자하기</strong></span>
                <p>시가총액 5천억원 이상 대형주 중에서 성장성이 높거나 실적이 턴어라운드 된 종목 위주로 선택하여 기업의 펀더멘탈 모멘텀에 투자합니다. 대형성장은 현재 주가 자체가 고평가 되어 있을지도 모르나 중장기적으로 추가적인 수익률을 추구합니다.</p>
                <ul>
                    <li>사이즈 score 5이상</li>
                    <li>성장성 score 4이상</li>
                    <li>거래량 score 3이상</li>
                    <li>모멘텀 score 2이상 4이하</li>
                </ul>
            </div>
        </div>
        <div id="line3" class="line">
            <div class="graphZone">
                <canvas id="g3" width="300" height="300"></canvas>
            </div>
            <div class="descriptionZone">
                <p class="descName">중소형밸류</p>
                <span><strong>작은 종목이지만 아직 정당한 평가를 받지 못한 종목에 투자하세요</strong></span>
                <p>사이즈(시가총액)이 작지만 저평가 되어 있는 종목 위주로 고릅니다. 적자 기업은 제외합니다. 성장성과 수익성과 같은 펀더멘탈 역시 우수하지만 현재 하락한 주가로 인하여 미래 상승여력이 충분한 종목을 선택합니다.</p>
                <ul>
                    <li>사이즈 score 2이상3이하</li>
                    <li>저평가 score 5이상</li>
                    <li>수익성 score 4이상</li>
                    <li>성장성 score 4이상</li>
                </ul>
            </div>
        </div>
        <div id="line4" class="line">
            <div class="graphZone">
                <canvas id="g4" width="300" height="300"></canvas>
            </div>
            <div class="descriptionZone">
                <p class="descName">컨트래리안</p>
                <span><strong>반등을 노리는 투자</strong></span>
                <p>컨트래리안 전략이란, 비록 최근에 주가가 크게 하락했지만 기업의 내재가치는 괜찮은 종목들을 선택하여 향후 반등을 노리는 전략입니다. 위험이 큰 전략이지만 그만큼 큰 수익을 얻을 수 있습니다.</p>
                <ul>
                    <li>거래량 score 3이상5이하</li>
                    <li>모멘텀 score 1이하</li>
                    <li>수익성 score 4이상</li>
                    <li>성장성 score 3이상</li>
                </ul>
            </div>
        </div>
        <div id="line5" class="line">
            <div class="graphZone">
                <canvas id="g5" width="300" height="300"></canvas>
            </div>
            <div class="descriptionZone">
                <p class="descName">로우볼</p>
                <span><strong>저변동성 팩터에 투자하기</strong></span>
                <p>2014년도에 가장 뜨거웠던 스마트베타가 '로우볼'이라는 사실을 아시나요? 학술적으로는 '하이리스크 하이리턴' 이란 말이 있습니다. 즉, 변동성이 높을 수록 높은 기대 수익율을 얻고 반대로 낮은 변동성은 낮은 기대수익률을 의미합니다. 다만 글로벌 시장 전체적으로 저변동성을 갖는 종목이 높은 수익률을 보이는 이상현상이 존재합니다. 로우볼 포트폴리오는 이를 위하여 낮은 변동성을 가진 종목을 종목을 선택합니다.</p>
                <ul>
                    <li>사이즈 score 2이상5이하</li>
                    <li>거래량 score 2이상</li>
                    <li>저평가 score 2이상</li>
                </ul>
            </div>
        </div>
        <b-button variant="outline-info" @click="moveBack">전략페이지로 돌아가기</b-button>
    </div>
</template>

<script>
    import Chart from 'chart.js'
    export default {
        name: "RecommendStrategy",
        mounted(){
            var ctx1=document.getElementById('g1')
            let radar1=new Chart(ctx1,{
                type: 'radar',
                data: {
                    labels: ['사이즈', '거래량', '모멘텀', '저평가', '성장성', '수익성'],
                    datasets: [
                        {
                            label: 'Min',
                            backgroundColor: 'rgba(00,181,198,0.2)',//'rgba(179,181,198,0.2)',
                            borderColor: '#6CC3D5',
                            pointBackgroundColor: '#6CC3D5',
                            pointBorderColor: '#fff',
                            data: [5,4,2,4,3,3]
                        },
                        {
                            label: 'Max',
                            backgroundColor: 'rgba(255,99,132,0.2)',
                            borderColor: '#FF7851',
                            pointBackgroundColor: '#FF7851',
                            pointBorderColor: '#fff',
                            data: [5,5,5,5,5,5]
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
            var ctx2=document.getElementById('g2')
            let radar2=new Chart(ctx2,{
                type: 'radar',
                data: {
                    labels: ['사이즈', '거래량', '모멘텀', '저평가', '성장성', '수익성'],
                    datasets: [
                        {
                            label: 'Min',
                            backgroundColor: 'rgba(00,181,198,0.2)',//'rgba(179,181,198,0.2)',
                            borderColor: '#6CC3D5',
                            pointBackgroundColor: '#6CC3D5',
                            pointBorderColor: '#fff',
                            data: [5,3,2,1,4,1]
                        },
                        {
                            label: 'Max',
                            backgroundColor: 'rgba(255,99,132,0.2)',
                            borderColor: '#FF7851',
                            pointBackgroundColor: '#FF7851',
                            pointBorderColor: '#fff',
                            data: [5,5,4,5,5,5]
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
            var ctx3=document.getElementById('g3')
            let radar3=new Chart(ctx3,{
                type: 'radar',
                data: {
                    labels: ['사이즈', '거래량', '모멘텀', '저평가', '성장성', '수익성'],
                    datasets: [
                        {
                            label: 'Min',
                            backgroundColor: 'rgba(00,181,198,0.2)',//'rgba(179,181,198,0.2)',
                            borderColor: '#6CC3D5',
                            pointBackgroundColor: '#6CC3D5',
                            pointBorderColor: '#fff',
                            data: [2,2,1,5,4,4]
                        },
                        {
                            label: 'Max',
                            backgroundColor: 'rgba(255,99,132,0.2)',
                            borderColor: '#FF7851',
                            pointBackgroundColor: '#FF7851',
                            pointBorderColor: '#fff',
                            data: [3,5,5,5,5,5]
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
            var ctx4=document.getElementById('g4')
            let radar4=new Chart(ctx4,{
                type: 'radar',
                data: {
                    labels: ['사이즈', '거래량', '모멘텀', '저평가', '성장성', '수익성'],
                    datasets: [
                        {
                            label: 'Min',
                            backgroundColor: 'rgba(00,181,198,0.2)',//'rgba(179,181,198,0.2)',
                            borderColor: '#6CC3D5',
                            pointBackgroundColor: '#6CC3D5',
                            pointBorderColor: '#fff',
                            data: [1,3,1,4,4,4]
                        },
                        {
                            label: 'Max',
                            backgroundColor: 'rgba(255,99,132,0.2)',
                            borderColor: '#FF7851',
                            pointBackgroundColor: '#FF7851',
                            pointBorderColor: '#fff',
                            data: [5,5,1,5,5,5]
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
            var ctx5=document.getElementById('g5')
            let radar5=new Chart(ctx5,{
                type: 'radar',
                data: {
                    labels: ['사이즈', '거래량', '모멘텀', '저평가', '성장성', '수익성'],
                    datasets: [
                        {
                            label: 'Min',
                            backgroundColor: 'rgba(00,181,198,0.2)',//'rgba(179,181,198,0.2)',
                            borderColor: '#6CC3D5',
                            pointBackgroundColor: '#6CC3D5',
                            pointBorderColor: '#fff',
                            data: [2,2,1,1,3,3]
                        },
                        {
                            label: 'Max',
                            backgroundColor: 'rgba(255,99,132,0.2)',
                            borderColor: '#FF7851',
                            pointBackgroundColor: '#FF7851',
                            pointBorderColor: '#fff',
                            data: [5,5,5,5,5,5]
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
        methods:{
            moveBack: function () {
                this.$router.push('/pages/Stat-Strategy')
            }
        }
    }
</script>

<style scoped>
.graphZone{
    float: left;
    width:35%
}
.descName{
    font-weight: bold;
    font-size: 20px;
}
.descriptionZone{
    float: right;
    width: 60%;
}
.line{
    height: 350px;
}
</style>