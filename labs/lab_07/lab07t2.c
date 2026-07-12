#include <stdio.h>

void add1(int *, int *);

int main() {
    int x = 1, y = 2;
    
    add1(&x, &y);
    printf("The sum is %d\n", x);

    return 0;
}

void add1(int *a, int *b) {
    *a = *a + *b;
}
