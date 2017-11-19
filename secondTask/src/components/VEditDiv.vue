
<!-- 实现contenteditable的双向绑定 -->
<template>
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

