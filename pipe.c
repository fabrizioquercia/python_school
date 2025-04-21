//Librerie
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

int main(){
    int fd[2];
    //dichiarazione delle variabili
    int num1,num2,somma=0;
    //pid=process ID temporaneo che ci servirà per la fork
    pid_t pid;
    //creazione della fork
    printf("1) Prima della Fork\n");
    pid=fork();
    printf("2) Dopo la fork\n");
    //primo controllo sul PID
    if(pid<0){
        //fallisce la fork, stampa dell'errore
        printf("errore!\n");
        //uscita anticipata
        exit(1);
    }
    else if (pid>0){
        //Processo Padre
        printf("3) Esecuzione del processo padre\n");

        //acquisizione dei due numeri da tastiera

        printf("Inserisci il primo numero:\n");
        scanf("%d",&num1);
        printf("Inserisci il secondo numero:\n");
        scanf("%d",&num2);

        //Creazione canale di comunicazione
        //chiudiamo il canale di comunicazione
        close(fd[0]);
        //Operazione di scrittura e preparazione del messaggio
        write(fd[1],&num1,sizeof(num1));

        write(fd[1], &num2, sizeof(num2));

        //chiudiamo il canale di scrittura
        close(fd[1]);

    }else{
        //Processo Figlio
        printf("4) Esecuzione del processo figlio\n");

        //Creazione canale di comunicazione
        //chiudiamo il canale di comunicazione
        close(fd[1]);
        //Operazione di lettura del messaggio
        read(fd[0],&num1,sizeof(num1));

        read(fd[0], &num2, sizeof(num2));

        //chiudiamo il canale di lettura
        close(fd[0]);

        //Somma dei due numeri
        somma=num1+num2;

        //stampa del risultato
        printf("La somma dei due numeri è: %d\n",somma);

    }
    return 0;
}