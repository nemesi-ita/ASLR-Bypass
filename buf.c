// Set ASLR!!!
// echo 2 > /proc/sys/kernel/randomize_va_space

#include <string.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]){

	char buff[159];
	if(argc <2){
   		printf("Syntax: %s <input string>\n", argv[0]);
		exit (0);

     	}
  strcpy(buff, argv[1]);
  return 0;

}