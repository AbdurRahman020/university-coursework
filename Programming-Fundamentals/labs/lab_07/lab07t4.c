#include<stdio.h>

int *foo1(int *);
int foo2(int *);

int main() {
    int i = 1;
	printf("The adress of i is %p\n", foo1(&i));
	printf("The value of i is %d\n", foo2(&i));

    return 0;
}

int *foo1(int *a) {
    return a;
}

int foo2(int *b) {
    return *b;
}
