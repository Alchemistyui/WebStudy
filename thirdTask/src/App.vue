<template>
  <div id="app">
    <div class="panel panel-primary">
      <div class="panel-heading">
        <h3 class="panel-title">Form Validation</h3>
      </div>
      <!-- 面板 -->
      <div class="panel-body">
        <!-- 输入表单 -->
        <form class="form-horizontal" role="form">


          <div class="form-group has-success">
            <label for="variable" class="col-sm-2 control-label">Variable</label>
            <div class="col-sm-10" >
              <input type="text" class="form-control" id="variable" placeholder="Enter a Variable" v-model="variable"  v-on:onclick="func()">
            </div>
          </div>


          <div class="form-group has-success">
            <label for="integer" class="col-sm-2 control-label">Integer</label>
            <div class="col-sm-10" >
              <input type="text" class="form-control" id="integer" placeholder="Enter an integer" v-model="integer"  v-on:onclick="func()">
            </div>
          </div>
          

          <div class="form-group"> 
            <label for="name" id="selectTitle" class="col-sm-2 control-label">Select</label> 
            <select class="form-control"  v-model="selected"> 
              <option disabled value="">Select</option>
              <option>1</option> 
              <option>2</option>
              <option>3</option>
              <option>4</option> 
              <option>5</option> 
            </select> 
          </div>




          <div class="form-group has-success">
            <label for="chinese" class="col-sm-2 control-label">中文</label>
            <div class="col-sm-10" >
              <input type="text" class="form-control"  id="chinese" placeholder="中文输入" v-model="chinese"  v-on:onclick="func()">
            </div>
          </div>



          <div class="form-group has-success">
            <label for="email" class="col-sm-2 control-label">E-mail</label>
            <div class="col-sm-10" >
              <input type="text" class="form-control" id="email" placeholder="Enter an email" v-model="email"  v-on:onclick="func()">
            </div>
          </div>


          <div class="form-group">
            <button type="button" class="btn btn-primary" v-on:click="submit">Submit</button>
          </div>
        </form>


        <table class="table">
          <tbody>
            <tr>
              <td>Variable</td>
              <td>{{tableVariable}}</td>
            </tr>
            <tr>
              <td>Integer</td>
              <td>{{tableInteger}}</td>
            </tr>
            <tr>
              <td>Select</td>
              <td>{{selected}}</td>
            </tr>
            <tr>
              <td>中文</td>
              <td>{{tableChinese}}</td>
            </tr>
            <tr>
              <td>E-mail</td>
              <td>{{tableEmail}}</td>
            </tr>
          </tbody>
        </table>
        

      </div>
    </div>
  </div>
</template>

<script>


export default {
  data () {
    return {
      variable: '',
      integer: '',
      chinese: '',
      email: '',
      selected: '',
      tableVariable: '',
      tableInteger: '',
      tableChinese: '',
      tableEmail: '',
      
    }
  },

  methods: {
    submit () {

     this.tableVariable = this.variable;
     this.tableInteger = this.integer;
     this.tableChinese = this.chinese;
     this.tableEmail = this.email;
   },
   emm() {
    alert("1");
  },
  emm2() {
    alert("2");
  }
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
  margin-top: 30px;
  width: 50%;
}
#app input {
  width: 80%;
}

#app select {
  width: 15%;
}

#selectTitle {
  /*display: inline-block;
  text-align: left;*/
  margin-left: 2%;
}



</style>
