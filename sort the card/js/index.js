function refresh(){
    var a = new Array();
    for(var i=0;i<20;i++){
    	a[i] = Math.random()*100;
    	a[i]=parseInt(a[i]);
    	var c = document.getElementById("left"+i);
    	c.innerHTML = "card"+a[i];
    	c.style.display = "block"
    	var x = document.getElementById("right"+i);
    	x.style.display = "none";
    }
}

function green() {
	alert('click');
	if(this.style.backgroundColor=== rgba(255,255,0,0.3)) {
		this.style.backgroundColor=rgba(0,255,0,0.3);
	} else {
		this.style.backgroundColor=rgba(255,255,0,0.3);
	}
}

function change(){
	//unfinished
}

