#include <stdio.h>

void printBitsChar(unsigned char value) {
    for (int i = 7; i >= 0; i--) {
        printf("%d", (value >> i) & 1);
    }
    printf(" ");
}

void printBitsUInt(unsigned int value) {
    for (int i = 31; i >= 0; i--) {
        printf("%d", (value >> i) & 1);
        if (i % 8 == 0)
            printf(" ");
    }
    puts("");
}

// function to pack four characters into an unsigned int
unsigned int packCharacters(char c1, char c2, char c3, char c4) {
    unsigned int packed = 0;

    packed = c1;                  
    packed = (packed << 8) | c2; 
    packed = (packed << 8) | c3;
    packed = (packed << 8) | c4;

    return packed;
}

int main() {
    char c1, c2, c3, c4;

    printf("Enter 4 characters: ");
    scanf(" %c %c %c %c", &c1, &c2, &c3, &c4);

    printf("\nCharacters in binary:\n");
    printf("c1 ('%c') = ", c1); printBitsChar((unsigned char)c1); printf("\n");
    printf("c2 ('%c') = ", c2); printBitsChar((unsigned char)c2); printf("\n");
    printf("c3 ('%c') = ", c3); printBitsChar((unsigned char)c3); printf("\n");
    printf("c4 ('%c') = ", c4); printBitsChar((unsigned char)c4); printf("\n");

    unsigned int packed = packCharacters(c1, c2, c3, c4);

    printf("\nPacked unsigned int in binary:\n");
    printBitsUInt(packed);
    printf("\nPacked value (hex): 0x%X\n", packed);

    return 0;
}
