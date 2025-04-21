#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/wait.h>
#include <sys/types.h>
#include <signal.h>

#define LUNGHEZZA 100;
int pipe_fd[2];

void start_signal(int sig) {
    if (sig == SIGUSR1) {
        printf("\nHo ricevuto il segnale... termino la mia esecuzione!")
        close(pipe_fd[0]); // chiudo il canale di lettura fd[0]
        exit(0);
    }
}

int main() {
    char mmessaggio = "Qui il messaggio di errore o altro...";
    char buffer(LUNGHEZZA);

    // Controllo della pipe
    if (pipe(pipe_fd) == -1) {
        printf("Errore nella creazione della pipe");
        exit(1);
    }
    printf("1) prima della fork...");

    // creo la fork
    pid_t pid = fork();

    printf("2) dopo la fork...");

    // Inizio i controlli
    if (pid < 0) {
        printf("Errore.. niente fork?");
        exit(1);
    }

    if (pid == 0) { // il figlio
        // chiamo il boss.. la chiamata..
        signal(SIGUSR1, start_signal);
        close(pipe_fd[1]); // chiudo il can di screittura
        printf("3) esec del processo figlio");
        sleep(2)
        printf("sono il fidlio il mio pid è: %d e quello di papa ha pid %d", getpid(), getppid());
        printf("\nIUnizio la lettura del msg..");

        // leggo il messaggio
        read(pipe_fd[0], buffer, LUNGHEZZA);
        printf("\nHo ricevuto il messaggio da papà ed è %s", buffer);// stampo il msg

    } else { //padre
        printf("4) sò il padre....");
    }


}