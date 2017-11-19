<template>
	<div id="createNew">

		<!-- input组 -->
		<p>Name: <input v-model="name"></p>
		<p>Age: <input v-model="age" placeholder="0"></p>
		<p>Sex: 
			<select v-model="selected">
				<option disabled value="">请选择</option>
				<option>Male</option>
				<option>Female</option>
			</select>
		</p>
		<button v-on:click="newItem">Create</button>


	</div>
</template>


<script>
// 引入eventBus中央事件总线，用于同级组件间的传值
import bus from '../assets/eventBus'

export default {
	data () {
		return {
			selected: '',
			name: '',
			age: ''
		}
	},
	methods: {
		newItem () {
			if (isNaN(this.age) || this.age === '') {
				alert('年龄须为数字，请重新输入~');
			}
			else if (this.selected === '') {
				alert('请选择性别~');
			}
			else {
				// $emit实例方法触发当前实例(这里的当前实例就是bus)上的事件,附加参数都会传给监听器回调
				bus.$emit('sendValue', this.name, this.age, this.selected);
				// 清空输入的数据
				this.name = '';
				this.age = '';
				this.selected = '';
			}

		}
	}
}
</script>