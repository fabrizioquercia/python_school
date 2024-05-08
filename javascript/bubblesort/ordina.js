function ordina(L){
	let LO=[];
	for (let i=0;i<N;i++){
		minimos = trova_min(L);
		LO.push(minimos[0]);
		L.splice(minimos[1],1);
	}

	return LO;
}

function trova_min(lista){
		let n=lista.length;
		let min=lista[0];
		let i_min=0;
		for (let i=1;i<n;i++) 
			if (L[i]<min){
				min=L[i];
				i_min=i;
			}
		return [min,i_min];
	}
