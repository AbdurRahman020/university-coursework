#include <stdio.h>

void add2(int *, int *);

int main() {
    int x = 1, y = 2;
    
    add2(&x, &y);
    
    return 0;
}

void add2(int *a, int *b) {
    printf("The sum is: %d\n", *a + *b);
}
