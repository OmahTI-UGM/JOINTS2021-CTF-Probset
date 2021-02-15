#include<signal.h>
#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>


#define CHUNK_SIZE  72

void kill_on_timeout(int sig) {
  if (sig == SIGALRM) {
    _exit(0);
  }
}


void nobaper() {
	setvbuf(stdout, NULL, _IONBF, 0);
	setvbuf(stdin, NULL, _IONBF, 0);
	setvbuf(stderr, NULL, _IONBF, 0);
	signal(SIGALRM, kill_on_timeout);
	alarm(60);
}

int main() {
  nobaper();

  int choice = -1;
  while(1) {
    show_menu();
    scanf("%d", &choice);
    switch(choice) {
      case 1:
        break;
      case 2:
        break;
      case 3:
        break;
      case 4:
        break;
      default:
        puts("Ummm, I don't what to do");
        break;
    }
  }

  return 0;
}
