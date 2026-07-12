#include <stdio.h>

int main() {
    int x = 1,  y = 2;
    int *a = &x,  *b = &y;

    printf("The sum is %d\n", *a + *b);

    return 0;
}
