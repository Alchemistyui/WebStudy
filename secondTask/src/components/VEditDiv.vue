
<!-- 实现contenteditable的双向绑定 -->
<template>
	<!-- v-html最好只用于自己写的东西，要是有别人写的东西容易被攻击 -->
	<!-- 这里可以考虑用钩子函数 -->
 <span contenteditable="true"
  v-html="innerText"
  
  @input="changeText"></span>
</template>
<script>
 export default {
 props: ['value'],
 data(){
  return {innerText:this.value}
 },
 methods:{
  changeText(){
  this.innerText = this.$el.innerHTML;
  this.$emit('input',this.innerText);
  }
 }
 }
</script>

