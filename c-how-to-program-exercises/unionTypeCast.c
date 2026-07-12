#include <stdio.h>

union Integer {
    char c;
    short s;
    int i;
    long b;
};

void printUnion(union Integer u) {
    printf("As char: %c\n", u.c);
    printf("As short: %hd\n", u.s);
    printf("As int: %d\n", u.i);
    printf("As long: %ld\n", u.b);
    printf("------\n");
}

int main() {
    union Integer u;

    printf("Enter a char: ");
    scanf(" %c", &u.c);
    printUnion(u);

    printf("Enter a short: ");
    scanf("%hd", &u.s);
    printUnion(u);

    printf("Enter an int: ");
    scanf("%d", &u.i);
    printUnion(u);

    printf("Enter a long: ");
    scanf("%ld", &u.b);
    printUnion(u);

    return 0;
}
