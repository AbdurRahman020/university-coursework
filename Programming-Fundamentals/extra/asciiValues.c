#include <stdio.h>

int main() {
    printf("ASCII values:\nUppercase letters:\n");
    for (char c = 'A'; c <= 'Z'; c++)
        printf("'%c' -> %d\n", c, c);

    printf("\nLowercase letters:\n");
    for (char c = 'a'; c <= 'z'; c++)
        printf("'%c' -> %d\n", c, c);

    printf("\nDigits 0-9:\n");
    for (char c = '0'; c <= '9'; c++)
        printf("'%c' -> %d\n", c, c);

    printf("\nSpecial characters:\n");
    for (char c = 32; c <= 47; c++)
        printf("'%c' -> %d\n", c, c);
	
    for (char c = 58; c <= 64; c++)
        printf("'%c' -> %d\n", c, c);
	
    for (char c = 91; c <= 96; c++)
        printf("'%c' -> %d\n", c, c);
	
    for (char c = 123; c <= 126; c++)
        printf("'%c' -> %d\n", c, c);

    return 0;
}
