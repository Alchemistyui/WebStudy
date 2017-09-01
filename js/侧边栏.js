window.onload = function() {
		var main = document.getElementById('main');
		var mainA = main.getElementsByClassName('mainA');
	
		
		for (var i = 0; i < mainA.length; i++) {
          alert(mainA[i].id);
			mainA[i].onclick = function() {
				alert(mainA[i].id);
			   var sub = mainA[i].getElementsByTagName('ul');
				alert(sub.className);
			   sub.style.display = block;
		}
		}
		
	}