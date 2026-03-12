const msgCalcolaNoTesto = "La casella delle cifre è vuota: Impossibile eseguire il calcolo.\n\nInserisci delle cifre con le quali vuoi eseguire le operazioni usando il tastierino numerico, poi premi di nuovo Calcola.";
const msgCalcolaNoOperando = "Non ci sono valori nella casella: Inserisci prima dei numeri, poi l'operando!";
const msgNoZeroIniziale = "Impossibile inserire uno 0 all'inizio:\n\nNon è possibile inserire cifre che iniziano con il numero zero ( 0 ).\nInserire solo cifre intere maggiori di zero.";


function resettaCalcolatrice() {
    var str = document.getElementById("schermo").value;
    console.log("strLen: " + str.length);
    if (str.length > 0) {
        setInterval(tornaIndietro, 25);
    }
}

// Resetta le caselle dei numeri e dell'operatore, per un nuovo calcolo
function nuovoCalcolo() {
    document.getElementById("schermo").value = "";
    //document.getElementById("schermo").setAttribute("rows", "3");
}

function addNumero(numero) {
    var oldNumero = document.getElementById("schermo").value;

    // Verifico che non ci sia lo 0 all'inizio del display
    if (numero == "0" && oldNumero == "") {
        if (noTesto(msgNoZeroIniziale)== false);
        return;
    }
    
    document.getElementById("schermo").value = oldNumero + numero
}

// Scrive l'operando
function addOperando(operando) {

    if (noTesto(msgCalcolaNoOperando) == false) {
        return;
    }

    var oldNumero = document.getElementById("schermo").value;
    var op = "";
    switch (operando) {
        case "piu": op = "+"; break;
        case "meno": op = "-"; break;
        case "per": op = "*"; break;
        case "diviso": op = "/"; break;
        default:
            op = "+";
        break;
    }
    document.getElementById("schermo").value = oldNumero + "" + op + "";
}

function tornaIndietro() {
    console.log("BACK!");
    var oldNumero = document.getElementById("schermo").value;
    var newNumero = oldNumero.substring(0, oldNumero.length - 1);
    document.getElementById("schermo").value = newNumero;
}

function calcola() {
    if (noTesto(msgCalcolaNoTesto) == false) {
        return;
    }
    var val = document.getElementById("schermo").value;
    var res = eval(val);
    var acc = "\n\n";

    console.log(val.length);
    console.log(res);


    if (val.length > 12) {
        acc = "\n";
    }

    var str = "" + val + acc + " =" + res;
    console.log("strlen=" + str.length);


    if (str.length > 30) {
        console.log("Troppo lungo = " + str.length);
        acc = "\n";
        //document.getElementById("schermo").setAttribute("rows", "4");
        //document.getElementById("schermo").setAttribute("style", "font-size: 24px;");

    }

    // Controllo di esempio: Se per caso ho più di 1 decimani nel risultato, allora ne mostro solo 2
    res = Number(res).toFixed(2);

    document.getElementById("schermo").value = document.getElementById("schermo").value + acc + " =" +  res;
}

// Funzioni di controllo
function noTesto(msg) {
    var sc = document.getElementById("schermo");
    if ( sc.value == "" ) {
        alert(msg);
        return false;
    }
    return true;
}
