#include <stdio.h>

int add(int, int);
void diff(int, int);
int prod(int, int);
void div();

int main() {
    int s;
    
    s = add(1, 2);
    printf("The sum is %d\n", s);
    
    diff(1,2);
    
    printf("The product of 1 and 2 is %d\n", prod(1,2));
    
    div();
    
    return 0;
}

int add(int a, int b) {
    return a + b;
}

void diff(int a, int b) {
    printf("The difference is %d\n", a - b);
}

int prod(int a, int b) {
    return a * b;
}

void div() {
    printf("1/2 = %f\n", 1.0/2);
}
