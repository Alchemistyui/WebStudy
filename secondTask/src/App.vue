<template>
  <div id="app">
    
    <create-new></create-new>
    <list></list>
    <!-- <App2></App2> -->

  </div>

</template>

<script>
import CreateNew from './components/CreateNew'
import List from './components/List'
import App2 from './App2'

export default {
  name: 'app',
  components: {
    List,
    CreateNew,
    App2
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
