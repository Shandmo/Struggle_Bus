#include <stdio.h>
#include <string.h>

#define MAX_LENGTH 1000
#define MIN_PRINTABLE_LENGTH 80
int main(){
	char line[MAX_LENGTH + 2];  // create array with size 1002
//	char line[MAX_LENGTH] ;  // create array with size 1000
	printf("Enter lines of text. (Ctrl + C on Linux or Ctrl + Z on Windows to exit)\n> ");
	while (fgets(line, sizeof(line), stdin) != NULL){ 
		if (strlen(line) <= MAX_LENGTH){
			if (strlen(line) > MIN_PRINTABLE_LENGTH){
				//strlen returns length of string, excluding the null terminator
				printf("%s", line);
			} else {
				printf("Line of text must be 80 characters or greater to be printed.\n");
			}
		} else {
			printf("Line exceeds maximum length and will not be printed.\n");
			int c;
			while ((c = getchar()) != '\n' && c != EOF);
		}
	}

}
