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
            <input v-model="date" type="date" placeholder="날짜">
            <p>초기자본금을 설정하세요</p>
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
    </div>
</template>

<script>
    export default {
        name: "StrategySimulator",
        data(){
            return{
                stockNum:[],
                date:'',
                budget:'',
                stockCode:[],
                stockList:[{code:1111, name:'t1',start_date:11111}, {code:2222, name:'t2',start_date:22222}],
                ratio:[],
                tmp:0

            }
        },
        methods:{
            addStock:function () {
                //종목추가
                this.stockNum.push(null);
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
                    //validation하고 맞으면 종목들에 해당하는 데이터로 그래프 만들기
                }
            }
        },
        computed:{
            setStockList:function () {
                //날짜선택한거 이후 모든 주식종목 받아서 stockList에 저장
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