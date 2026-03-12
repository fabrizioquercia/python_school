function saluta() {
    let obj = document.getElementById("p_saluto");
    obj.innerHTML="Ciao <strong>mondo!</strong>";
}

function saluta2() {
    let obj = document.getElementById("p_saluto");
    obj.innerHTML="Vi <span style='color: red'>siete</span> <strong>divertiti?</strong>";
}

function ricarica() {
    document.location.reload();
}

function coloraSfondo(val) {
    let color = "ffffff";
    switch (val) {
        case 1:  color = "ececec"; break;
        case 2:  color = "55ff55"; break;
        case 3:  color = "dd4455"; break;
        default: color = color; break;
    }
    document.body.style.backgroundColor = "#"+color;
}

function numb() {
    
    //alert("numb");
    let x = document.getElementById("numero").value;
    //alert(x);
    let text = "";
    if ( isNaN(x) || x <= 0 || x > 20  ) {
        text = "Input nno valido";
    } else {
        text = "Input OK";
    }
    //alert(text);
    document.getElementById("esempio").innerHTML = text;

    

}

function giochino() {
    //let errori = 0;
    const valoreFisso = 34;

    let x = document.getElementById("numero").value;
    alert(x);
    let text = "";
    if ( isNaN(x) || x <= 0 || x != valoreFisso  ) {
        text = "Non hai indovinato (34)";
        document.getElementById("numero").value = "";
    } else {
        text = "EUREKAAAAAAA";
    }
    document.getElementById("esempio").innerHTML = text;

}


