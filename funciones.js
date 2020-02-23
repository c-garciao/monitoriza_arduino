setInterval(function(){
	var xhr = new XMLHttpRequest();
		xhr.onreadystatechange = function(){
			if(this.readyState == 4 && this.status ==200){
				document.getElementById("valor_temp").innerHTML = this.responseText;
				var patata = this.responseText;
				var humedad = patata.split(";")[0];
				var temperatura = patata.split(";")[1];
				console.log(humedad, temperatura);
				document.getElementById("valor_temp").innerHTML = temperatura;
				document.getElementById("valor_humedad").innerHTML = humedad;
			}
		}; 
		xhr.open ("GET", "./datos.txt", true);
		xhr.send();
},1000);

