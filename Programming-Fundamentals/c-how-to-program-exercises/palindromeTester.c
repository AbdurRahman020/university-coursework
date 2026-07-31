#include <stdio.h>

int main() {
    int num, originalNum, digit1, digit2, digit3, digit4, digit5;

    printf("Enter a five-digit integer: ");
    scanf("%d", &num);

    originalNum = num;

    digit1 = num / 10000;
    digit2 = (num / 1000) % 10;
    digit3 = (num / 100) % 10;
    digit4 = (num / 10) % 10;
    digit5 = num % 10;

    if (digit1 == digit5 && digit2 == digit4)
        printf("The number %d is a palindrome.\n", originalNum);
    else
        printf("The number %d is not a palindrome.\n", originalNum);

    return 0;
}
