#include <stdio.h>

void printBits(unsigned int value) {
    for (int i = sizeof(unsigned int) * 8 - 1; i >= 0; i--) {
        printf("%d", (value >> i) & 1);
        if (i % 8 == 0)
            printf(" ");
    }
    puts("");
}

unsigned int power2(unsigned int number, unsigned int pow) {
    // number * (2^pow)
    return number << pow;  
}

int main() {
    unsigned int number, pow;

    printf("Enter a non-negative integer: ");
    scanf("%u", &number);
    printf("Enter the power (non-negative integer): ");
    scanf("%u", &pow);

    unsigned int result = power2(number, pow);

    printf("\nBefore shift (number = %u):\n", number);
    printBits(number);
    printf("After left shift by %u (number * 2^%u = %u):\n", pow, pow, result);
    printBits(result);

    return 0;
}
