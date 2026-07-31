#include <stdio.h>

int main() {
    int a, b, c;

    printf("Enter value of a: ");
    scanf("%d", &a);

    printf("Enter value of b: ");
    scanf("%d", &b);

    printf("Enter value of c: ");
    scanf("%d", &c);

    if (a >= b) {
        if (a >= c)
            printf("a has the maximum value of %d\n", a);
        else
            printf("c has the maximum value of %d\n", c);
    }
    else if (b >= c)
        printf("b has the maximum value of %d\n", b);
    else
        printf("c has the maximum value of %d\n", c);

    return 0;
}
