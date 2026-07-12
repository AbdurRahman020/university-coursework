#include <stdio.h>

int main() {
    int x, bound1, bound2, lower, upper;

    printf("Enter three integers (x, bound1, bound2): ");
    scanf("%d %d %d", &x, &bound1, &bound2);

    if (bound1 < bound2) {
        lower = bound1;
        upper = bound2;
    } else {
        lower = bound2;
        upper = bound1;
    }

    if (x < lower)
        printf("%d\n", lower);
    else if (x > upper)
        printf("%d\n", upper);
    else
        printf("%d\n", x);

    return 0;
}
