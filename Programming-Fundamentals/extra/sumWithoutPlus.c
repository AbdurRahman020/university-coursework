#include <stdio.h>

int add(int a, int b) {
    while (b != 0) {
        int carry = a & b;
        a = a ^ b;
        b = carry << 1;
    }
    return a;
}

int main() {
    int num1, num2;
    scanf("%d%d", &num1, &num2);

    int sum = 0;
    printf("The sum is: %d\n", add(num1, num2));
}
