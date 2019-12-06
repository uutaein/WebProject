<template>
    <div id="Dashboards">
        <p class="title">Welcome to My Asset</p>
        <button class="circles" id="Btn0" @click="movetoStrategySimulator" @mouseover="mouseoverDescription(0)" @mouseleave="mouseleaveDescription(0)">Strategy Simulator</button>
        <button class="circles" id="Btn1" @click="movetoStatStrategy" @mouseover="mouseoverDescription(1)" @mouseleave="mouseleaveDescription(1)">Stat Strategy Simulator</button>
        <button class="circles" id="Btn2" @click="movetoInvestGame" @mouseover="mouseoverDescription(2)" @mouseleave="mouseleaveDescription(2)">Investment Game</button>
    </div>
</template>

<script>
        import router from 'vue-router'

        export default {
            name:'Dashboards',
            data: () => ({
            }),
            mounted(){
                return function mouseoverdescription(i) {
                    var description=[]
                    description.push("포트폴리오 성과 추출기")
                    description.push("주식스탯으로 세워보는 나만의 전략")
                    description.push("모의 주식투자")
                    console.log(description[0])
                    document.getElementById('Btn'+i).innerText=description[i];
                }
            },
            methods: {
                movetoStrategySimulator: function () {
                    this.$router.push('/pages/Strategy-Simulator');
                },
                movetoStatStrategy: function () {
                    this.$router.push('/pages/Stat-Strategy');
                },
                movetoInvestGame: function () {
                    this.$router.push('/pages/Investment-Game');

                },
                mouseoverDescription: function (i) {
                    var description=[]
                    description.push("포트폴리오 성과 추출기")
                    description.push("주식스탯으로 세워보는 나만의 전략")
                    description.push("모의 주식투자")
                    document.getElementById('Btn'+i).innerText=description[i];
                },
                mouseleaveDescription: function (i) {
                    var description=[]
                    description.push("Strategy Simulator")
                    description.push("Stat Strategy")
                    description.push("Invest Game")
                    document.getElementById('Btn'+i).innerText=description[i];
                }
            },

        }


</script>

<style>
.circles{
    width: 300px;
    height: 300px;
    margin: 100px;
    text-align: center;
    border-radius: 50%;
    padding-top: auto;
    font-weight: bold;
    font-size: 30px;
    font-family: Apple;
}
.title{
    text-align: center;
    font-size: 36px;
    font-family: Apple;
    color: #69aa8a;
    font-weight: bold;
}
#Btn0{
    background-color: #e3716c;
    color: white;
}
#Btn1{
    background-color: #4709ac;
    color: white;
}

#Btn2{
    background-color: #3ac18c;
    color: white;
}
</style>
