<template>
	<div id="list">


		<!-- 复选框标题 -->
		<p><input type="checkbox" v-model="allChecked">
			<span>Name</span> 
			<span>Age</span> 
			<span>Sex</span> 
			<span>Delete</span>
			

		</p>



		<!-- 复选框 -->
		<ul>
			<!-- 最好列表要用复数 -->
			<li v-for="(man, index) in list"  v-bind:class="{active: man.isActive}">
				<input type="checkbox" :value="man.name"  v-model="checked" v-on:click="itemIsActive(man)"> 
				<!-- v-on:click="isActive($event)"-->
				<!-- 实现数据双向绑定的组件 -->
				<v-edit-div v-model='man.name'></v-edit-div>
				<v-edit-div v-model='man.age'></v-edit-div>
				<v-edit-div v-model='man.sex'></v-edit-div>
				<button v-on:click="deletePerson(man.index)">Delete</button>
			</li>
		</ul>

		


	</div>
</template>


<script>
// 使用let和const替代var以防止作用域的问题

import bus from '../assets/eventBus'
// 注册一个组件用于实现contenteditable的双向绑定
import VEditDiv from './VEditDiv'

export default {

	components: {
		VEditDiv
	},

	data () {
		return {

			name: '',
			age: '',
			sex: '',

			list: [
			{ name:'Tom', age: 10, sex: 'Male', isActive: false },
			{ name:'Mary', age: 20, sex: 'Female', isActive: false }
			],
			checked: [],
			editable: false
			
		}
	},
    // mounted:是一个Vue生命周期中的钩子函数，用于组件间的传值
    mounted () {
    	var self = this;
		// $on:监听当前实例上的自定义事件
		bus.$on('sendValue', function(name, age, sex){
			self.name = name;
			self.age = age;
			self.sex = sex;
			self.list.push({name: self.name, age: self.age, sex: self.sex});
		});

	},

	methods:{

		deletePerson: function(index){
			this.list.splice(index,1);
		},


        //虽然这个代码无卵用写得不好，但是event的使用这一点还是值得学习的
		// 使用javascript有关event标准属性
		// isActive: function(event) {
		// 	// currentTarget 事件属性返回其监听器触发事件的节点，即当前处理该事件的元素、文档或窗口。
		// 	var li = event.currentTarget;

		// 	li.isActive = !(li.isActive);
		// 	alert(li.isActive);

		// 	document.querySelector(li).setAttribute('style', 'background:#fff');

		// },


		itemIsActive: function (li) {
			li.isActive = !(li.isActive);
		}

	},


	// watch的话会导致代码的冗余，经过计算得出的最好用计算属性
    // 计算属性用于实现复选框全选功能
    computed: {
    	allChecked: {
    		// 检查下面的属性
    		get: function() {
    			return this.checkedCount == this.list.length;
    		},
    		// 为属性赋值不是直接赋而是调用函数
    		set: function(value) {
    			if (value) {
    				this.checked = this.list.map(function(item) {
    					return item.name
    				})
    			} else {
    				this.checked = []
    			}
    		}
    	},
    	checkedCount: {
    		get: function() {
    			return this.checked.length;
    		}
    	}
    }

}

</script>

<style type="text/css">
#list {
	padding: 50px;
}

#list p {
	width: auto;
	padding-left: 15px;
	border-bottom: 1px solid #eee;
	padding-bottom: 10px;
}

span {
	display: inline-block;
	width: 70px;
	padding-left: 50px;
}

ul {
	padding: 0px;
	margin: 0px;
	list-style-type: none;
	
}

ul li {
	width: auto;
	padding: 10px;
	padding-left: -10px;
	border-bottom: 1px solid #eee;
	
}

ul li span {
	text-align: left;
}

button {
	margin-left: 50px;
}

.active {
	background-color: #eee;
}
</style>