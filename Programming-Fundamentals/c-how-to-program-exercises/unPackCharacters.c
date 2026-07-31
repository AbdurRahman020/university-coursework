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

void unpackCharacters(unsigned int packed) {
    unsigned int mask1 = 0xFF000000;
    unsigned int mask2 = 0x00FF0000;
    unsigned int mask3 = 0x0000FF00;
    unsigned int mask4 = 0x000000FF;

    char c1 = (char)((packed & mask1) >> 24);
    char c2 = (char)((packed & mask2) >> 16);
    char c3 = (char)((packed & mask3) >> 8);
    char c4 = (char)(packed & mask4);

    printf("\nPacked unsigned int (binary):\n");
    printBitsUInt(packed);

    printf("\nUnpacked characters in binary:\n");
    printf("c1 ('%c') = ", c1); printBitsChar((unsigned char)c1); printf("\n");
    printf("c2 ('%c') = ", c2); printBitsChar((unsigned char)c2); printf("\n");
    printf("c3 ('%c') = ", c3); printBitsChar((unsigned char)c3); printf("\n");
    printf("c4 ('%c') = ", c4); printBitsChar((unsigned char)c4); printf("\n");
}

int main() {
    unsigned int packed = 0x41424344;

    unpackCharacters(packed);

    return 0;
}
