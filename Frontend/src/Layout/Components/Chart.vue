<template>
        <div>
        test입니다.
        <!-- object value -->
        <model-select :options="options"
                                v-model="item"
                                placeholder="select item">
         </model-select>
    
       
         <!-- string value -->

        <button @click="addoption"></button>
         {{item}}
         </div>
        
</template>

<script>
  import { ModelSelect } from 'vue-search-select'
  import 'vue-search-select/dist/VueSearchSelect.css'
    export default {
    data () {
      return {
        options: [],
        item : ''
           
      }
    },
    methods: {
      reset () {
        this.item = {}
      },
      selectFromParentComponent1 () {
        // select option from parent component
        this.item = this.options[0]
      },
      reset2 () {
        this.item2 = ''
      },
      selectFromParentComponent2 () {
        // select option from parent component
        this.item2 = this.options2[0].value
      },
      addoption(){
          for(var i=0;i<800;i++){
              this.options.push({value : i,text:"["+i+"]" +"숫자는" + i +"입니다."});
          }
      }
    },
    components: {
      ModelSelect
    }
    }
</script>

<style>

</style>