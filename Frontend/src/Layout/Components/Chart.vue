<template>
    <div class="app-footer">
        <h1>Chart Vue 입니다</h1>
        <input v-model="start" placeholder="YYYY-MM-DD">
        {{start}}
       <button v-on:click="create()">제출</button>
    </div>
</template>

<script>
export default{
    data(){
        return{
            start : ""
        }
    },
    methods:{
        create(){
            this.$axios.post('test',{start:this.start}).then(function(response){
                console.log("response : " + response[0]);
                var test_sql = response;
                console.log(test_sql.data[0].open);
            })
        }
    }
    
}
</script>
