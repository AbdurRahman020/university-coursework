#include <stdio.h>

void printBits(unsigned int value) {
    for (int i = 31; i >= 0; i--) {
        printf("%d", (value >> i) & 1);
        if (i % 8 == 0)
            printf(" ");
    }
    puts("");
}

unsigned int reverseBits(unsigned int num) {
    unsigned int reversed = 0;

    for (int i = 0; i < 32; i++) {
        // shift left to make room
        reversed <<= 1;
        // add the lowest bit of num
        reversed |= (num & 1);
        // shift num right to get next bit
        num >>= 1;
    }

    return reversed;
}

int main() {
    unsigned int value;

    printf("Enter an unsigned integer: ");
    scanf("%u", &value);
    printf("\nOriginal bits:\n");
    printBits(value);

    unsigned int reversed = reverseBits(value);

    printf("\nReversed bits:\n");
    printBits(reversed);
    printf("\nOriginal value: %u\n", value);
    printf("Reversed value: %u\n", reversed);

    return 0;
}
