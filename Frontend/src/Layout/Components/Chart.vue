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
    methods : 
    {
        create()
        {
            this.$store.dispatch('addDataToChart');
        }
    },
    mounted()
    {

    }
    
}
</script>
