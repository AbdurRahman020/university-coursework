#include <stdio.h>

union FloatingPoint {
    float f;
    double d;
    long double x;
};

void printUnion(union FloatingPoint u) {
    printf("As float: %f\n", u.f);
    printf("As double: %lf\n", u.d);
    printf("As long double: %Lf\n", u.x);
    printf("------\n");
}

int main() {
    union FloatingPoint u;

    printf("Enter a float: ");
    scanf("%f", &u.f);
    printUnion(u);

    printf("Enter a double: ");
    scanf("%lf", &u.d);
    printUnion(u);

    printf("Enter a long double: ");
    scanf("%Lf", &u.x);
    printUnion(u);

    return 0;
}
