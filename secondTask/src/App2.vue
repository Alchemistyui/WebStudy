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


          <div v-bind:class="[formGroup, inputState[0]]">
            <label for="variable" class="col-sm-2 control-label">Variable</label>
            <div class="col-sm-10" >
              <input type="text" class="form-control" id="variable" placeholder="Enter a Variable" v-model="variable"  v-on:input="variableVerify()">
            </div>

            <div class="form-group has-error">
              <label class="control-label" for="inputError">{{errorLabel[0]}}</label>
            </div>
          </div>


          <div v-bind:class="[formGroup, inputState[1]]">
            <label for="integer" class="col-sm-2 control-label">Integer</label>
            <div class="col-sm-10" >
              <input type="text" class="form-control" id="integer" placeholder="Enter an integer" v-model="integer"  v-on:blur="integerVerify()">
            </div>

            <div class="form-group has-error">
              <label class="control-label" for="inputError">{{errorLabel[1]}}</label>
            </div>
          </div>
          

          <div v-bind:class="[formGroup, inputState[2]]"> 
            <label for="name" id="selectTitle" class="col-sm-2 control-label">Select</label> 
            <select class="form-control"  v-model="selected" v-on:change="selectVertify()"> 
              <option disabled value="">Select</option>
              <option>1</option> 
              <option>2</option>
              <option>3</option>
              <option>4</option> 
              <option>5</option> 
            </select> 

            <div class="form-group has-error">
              <label class="control-label" for="inputError">{{errorLabel[2]}}</label>
            </div>
          </div>




          <div v-bind:class="[formGroup, inputState[3]]">
            <label for="chinese" class="col-sm-2 control-label">中文</label>
            <div class="col-sm-10" >
              <input type="text" class="form-control"  id="chinese" placeholder="中文输入" v-model="chinese" v-on:input="chineseVertify()">
            </div>

            <div class="form-group has-error">
              <label class="control-label" for="inputError">{{errorLabel[3]}}</label>
            </div>
          </div>



          <div v-bind:class="[formGroup, inputState[4]]">
            <label for="email" class="col-sm-2 control-label">E-mail</label>
            <div class="col-sm-10" >
              <input type="text" class="form-control" id="email" placeholder="Enter an email" v-model="email"  v-on:blur="emailVertify()">
            </div>

            <div class="form-group has-error">
              <label class="control-label" for="inputError">{{errorLabel[4]}}</label>
            </div>
          </div>


          <div class="form-group">
            <button type="button" class="btn btn-primary" v-on:click="submit">Submit</button>
          </div>
        </form>


        <table v-bind:class="[table, showTable]">
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
              <td>{{tableSelected}}</td>
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
      tableSelected: '',
      tableChinese: '',
      tableEmail: '',
      table: 'table',
      showTable: 'unShow',
      errorLabel: ['','','','',''],
      formGroup: 'form-group',
      inputState: ['','','','','']
      
    }
  },

  methods: {
    submit () {
      this.variableVerify();
      this.integerVerify();
      this.selectVertify();
      this.emailVertify();
      this.chineseVertify();

      for(var i = 0; i < 5; i++) {
        if(this.errorLabel[i] != ''){
          alert('请正确填写');
          return ;
        }
      }
      this.showTable = '';
      this.tableVariable = this.variable;
      this.tableInteger = this.integer;
      this.tableSelected = this.selected;
      this.tableChinese = this.chinese;
      this.tableEmail = this.email;
      this.variable = '',
      this.integer = '',
      this.selected = '',
      this.chinese = '',
      this.email = '',
      this.inputState = ['','','','','']
    },
    variableVerify() {
      var right = /^[a-zA-Z\$_][a-zA-Z\d_]*$/;
      if (this.variable === '') {
        this.inputState[0] = 'has-error';
        this.errorLabel[0] = 'input can\'t be empty' ;
      }

      else if(right.test(this.variable)) {
        this.inputState[0] = 'has-success';
        this.errorLabel[0] = '';
      }
      else {
        this.inputState[0] = 'has-error';
        this.errorLabel[0] = 'please enter the right variable  name';
      }
    },

    integerVerify() {
      var right = /^[-+]?[0-9]*$/;
      if (this.integer === '') {
        this.inputState[1] = 'has-error';
        this.errorLabel.splice(1, 1, 'input can\'t be empty');
      }
      else if (right.test(this.integer)) {
        this.errorLabel.splice(1, 1, '');
        this.inputState[1] = 'has-success';
      }

      else {
        this.inputState[1] = 'has-error';
        this.errorLabel.splice(1, 1, 'please enter the right integer');
      }
    },
    selectVertify() {
      if(this.selected === '') {
        this.inputState[2] = 'has-error';
        this.errorLabel.splice(2, 1, 'input can\'t be empty');
      }
      else {
        this.inputState[2] = 'has-success';
        this.errorLabel.splice(2, 1, '');
      }
    },
    chineseVertify() {
      var right =  /[\u4e00-\u9fa5]/;

      if (this.chinese === '') {
        this.inputState[3] = 'has-error';
        this.errorLabel.splice(3, 1, 'input can\'t be empty');
      }
      else if (right.test(this.chinese)) {
        this.errorLabel.splice(3, 1, '');
        this.inputState[3] = 'has-success';
      }

      else {
        this.inputState[3] = 'has-error';
        this.errorLabel.splice(3, 1, 'please enter chinese');
      }
    },
    emailVertify() {
      var right =   /^[a-z0-9]+([._\\-]*[a-z0-9])*@([a-z0-9]+[-a-z0-9]*[a-z0-9]+.){1,63}[a-z0-9]+$/;

      if (this.email === '') {
        this.inputState[4] = 'has-error';
        this.errorLabel.splice(4, 1, 'input can\'t be empty');
      }
      else if (right.test(this.email)) {
        this.errorLabel.splice(4, 1, '');
        this.inputState[4] = 'has-success';
      }

      else {
        this.inputState[4] = 'has-error';
        this.errorLabel.splice(4, 1, 'please enter the right email adress');
      }
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
  margin-left: 2%;
}

.unShow {
  display: none;
}



</style>
