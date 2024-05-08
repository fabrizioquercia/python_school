function pressButton2(){

    let x=document.getElementById('i_num').value;
    let y=document.getElementById('sb1').value;
    document.getElementById(y).innerHTML=x;
    document.getElementById(y).style.backgroundColor="red";
}

function pressButton(){
    let x=document.getElementById('i_num').value; 
    let y=document.getElementById('sb1').value;

    
    switch (y) {
        case "box-1":
            document.getElementById('box-1').innerHTML=x;
            document.getElementById('box-1').style.backgroundColor="red"
            break;
        case "box-2":
            document.getElementById('box-2').innerHTML=x;
            document.getElementById('box-2').style.backgroundColor="red"
            break;
        case "box-3":
            document.getElementById('box-3').innerHTML=x;
            document.getElementById('box-3').style.backgroundColor="red"
            break;
        case "box-4":
            document.getElementById('box-4').innerHTML=x;
            document.getElementById('box-4').style.backgroundColor="red"
            break;
        case "box-5":
            document.getElementById('box-5').innerHTML=x;
            document.getElementById('box-5').style.backgroundColor="red"
            break;
        default:
            break;
    }

    let sb1 = document.getElementById("sb1");
    let lng = sb1.length;

    if (sb1.selectedIndex < lng-1) {
        sb1.selectedIndex += 1;
    }

    document.getElementById('i_num').value="";
    document.getElementById('i_num').focus();
    

}

function primoCiclo(){
    let scambio = true;
    while (scambio){
        scambio = false;
        for (let i=2; i<=5;i++){
            let s = 'box-'+i;
            let p = 'box-'+(i-1);
            succ=document.getElementById(s);
            prec = document.getElementById(p);
            x = Number(succ.innerHTML);
            y = Number(prec.innerHTML);
            if (x<y){
                scambio= true;
                succ.style.backgroundColor="yellow";
                prec.style.backgroundColor="yellow";
                let appo = succ.innerHTML;
                succ.innerHTML=prec.innerHTML;
                prec.innerHTML=appo;
            }
        }
    }  
    
    for (let i = 1; i <= 5; i++) {
        let box = document.getElementById("box-"+i);
        box.style.border = "6px solid #FF0000";
        box.style.backgroundColor="green";
        box.style.color="white";
        box.style.textAlign="center";    
    }




    document.getElementsByClassName("grid centrata")[0].style.backgroundColor="black";
}