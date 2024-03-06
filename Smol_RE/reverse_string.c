#include <stdio.h>
#include <string.h>
//Write a function reverse(s) that reverses the character string s, that reverses its input a line at a time.
int main(){
	char string[100];
	char reverse_string[100];
	int i = 0;
	int j = 0;
	// Grab each character of the string one at a time.
	printf("Enter a string: ");
	fgets(string, sizeof(string), stdin);
	
	// Remove the null terminator so it's not added to beginning of reverse string.
	string[strcspn(string, "\n")] ='\0';
	int len = strlen(string);
	
	for (i = len - 1, j = 0; i >= 0; i--, j++){
		reverse_string[j] = string[i];
	}
	// Add back in the null terminator
	reverse_string[j] = '\0';
	printf("Reversed string: %s\n", reverse_string);
	return 0;
}
