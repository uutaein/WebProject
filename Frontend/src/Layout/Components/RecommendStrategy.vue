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
        <div id="line2" class="line"></div>
        <div id="line3" class="line"></div>
        <div id="line4" class="line"></div>
        <div id="line5" class="line"></div>
    </div>
</template>

<script>
    import Chart from 'chart.js'
    export default {
        name: "RecommendStrategy"
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