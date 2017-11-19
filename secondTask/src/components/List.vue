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
			<li v-for="(man, index) in list">
				<input type="checkbox" :value="man.name"  v-model="checked" v-on:click="isActive($event)">
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
			alert(this.list.length);
			// alert(self.name + self.age+self.sex);
			this.list.push({ name:'Tom', age: 10, sex: 'Male' });
			alert(this.list.length);
			// ({name: self.name, age: self.age, sex: self.sex});

		});

	},

	methods:{

		deletePerson: function(index){
			this.list.splice(index,1);
		},

		isActive: function(li) {
			if (li.isActive) {
				li.isActive = false;
			}
			li.isActive = !(li.isActive);
			alert(li.isActive);
			document.querySelector(li).setAttribute('style', 'background:#fff');

		}
	},

    // 计算属性用于实现复选框全选功能
    computed: {
    	allChecked: {
    		get: function() {
    			return this.checkedCount == this.list.length;
    		},
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