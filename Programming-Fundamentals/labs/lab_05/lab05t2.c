#include <stdio.h>

int calculate_module(int, int);

int main() {
    int dividend, divisor;
    
    printf("Enter the dividend: ");
    scanf("%d", &dividend);

    printf("Enter the divisor: ");
    scanf("%d", &divisor);

    printf("The modulo is %d\n", calculate_module(dividend, divisor));

    return 0;
}

int calculate_module (int dividend, int divisor) {
    int x = -1;
    int y;

    if (dividend >= 0) {
        return dividend % divisor;
    } 
    else {
        do {
            y = divisor * x;
            x -= 1;
        } while (y > dividend);

        return (-y + dividend);
    }
}