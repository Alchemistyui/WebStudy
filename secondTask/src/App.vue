<template>
  <div id="app">
    
    <create-new></create-new>
    <list></list>
<!-- 数组push没有实现，传值成功 -->
<!-- 选中复选框时改变颜色没有实现 -->
  </div>

</template>

<script>
import CreateNew from './components/CreateNew'
import List from './components/List'

export default {
  name: 'app',
  components: {
    List,
    CreateNew
  }
}




</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin: 0 auto;
  margin-top: 60px;
  width: 700px;

}
</style>
