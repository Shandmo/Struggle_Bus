#include <stdio.h>
#include <stdlib.h>

int main(){
    int n, i;
    char *arr;

    printf("Enter the number of characters to store: ");
    scanf("%d", &n); //n == size
    arr = (char*)malloc(n*sizeof(char));
    printf("Enter the string: ");
    for(i=0; i < n; i++){
        scanf(" %c", arr+i); //add each character one at a time.
    }
    printf("\nThe string entered is: \n\n");

    for(i=0; i < n; i++){
        printf("%c ", arr[i]); //print the index of the array one at a time.
    }
    printf("\nThe element at index 2: %c ", arr[2]);
    return 0;
}
/*
https://www.scaler.com/topics/character-array-in-c/
https://stackoverflow.com/questions/2094666/pointers-in-c-when-to-use-the-ampersand-and-the-asterisk
int* p; variable p is pointer to integer type
int i; integer value
You turn pointers in values with *
int i2 = *p; integer i2 is assigned with the integer value that p is pointing to.
You turn values into pointers with &
int* p2 = &i; pointer p2 will point to the integer i
In the case of arrays:
int a[2];
int i = *a; the value of the first element of a
int i2 = a[0]; i2 also equals the first value of a
int i2 = a[1]; the value of the second element.
This means the index operator [] is a special form of the * operator.
a[i] == *(a + i); These two statements are the same thing.
*/