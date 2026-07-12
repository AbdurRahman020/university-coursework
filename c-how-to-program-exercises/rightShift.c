#include <stdio.h>
#include <limits.h>

void printBits(unsigned int value) {
    for (int i = sizeof(unsigned int) * 8 - 1; i >= 0; i--) {
        printf("%d", (value >> i) & 1);
        if (i % 8 == 0)
            printf(" ");
    }
    puts("");
}

int main() {
    int num;

    printf("Enter an integer: ");
    scanf("%d", &num);
    printf("\nBefore shifting:\n");
    printBits((unsigned int)num);

    int shifted = num >> 4;

    printf("After right shift by 4 bits:\n");
    printBits((unsigned int)shifted);
    printf("\nOriginal value: %d\n", num);
    printf("Shifted value : %d\n", shifted);

    return 0;
}
