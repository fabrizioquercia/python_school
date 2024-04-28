//connessione javascript con flask
function getlibri(){
    console.log('dd');
    const xhttp = new XMLHttpRequest();
		xhttp.onload = function() {
			document.getElementById("dati").innerHTML = this.responseText;
		}
		xhttp.open("GET", "http://127.0.0.1:5000/");
		xhttp.send();
		
}
getlibri()