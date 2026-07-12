#include <stdio.h>

int main() {
    int x, y, i = 1, power = 1;

    printf("Enter first integer: ");
    scanf("%d", &x);

    printf("Enter second integer: ");
    scanf("%d", &y);

    while (i <= y) {
        power *= x;
        i++;
    }

    printf("%d to the power of %d is %d\n", x, y, power);

    return 0;
}
