#include <stdio.h>

#define FACTORIAL
// #define ESTIMATE_E
// #define COMPUTE_EX

double factorial(int n) {
    double result = 1;
    for (int i = 1; i <= n; i++) {
        result *= i;
    }
    
    return result;
}

#ifdef FACTORIAL
// (a) compute the factorial of a number
int main() {
    int n;
    printf("Enter a non-negative integer: ");
    scanf("%d", &n);

    if (n < 0) {
        printf("Factorial is not defined for negative numbers.\n");
    } else {
        printf("Factorial of %d is %.0f\n", n, factorial(n));
    }

    return 0;
}
#endif

#ifdef ESTIMATE_E
// (b) estimate the value of e using the series
double estimate_e(int terms) {
    double sum = 1.0;
    for (int i = 1; i < terms; i++) {
        sum += 1.0 / factorial(i);
    }
    return sum;
}

int main() {
    int terms;
    printf("Enter the number of terms to estimate e: ");
    scanf("%d", &terms);

    double e = estimate_e(terms);
    printf("Estimated value of e using %d terms: %.10f\n", terms, e);

    return 0;
}
#endif

#ifdef COMPUTE_EX
// (c) compute the value of e^x using the series
double compute_ex(double x, int terms) {
    double sum = 1.0; 
    double power_of_x = 1.0;

    for (int i = 1; i < terms; i++) {
        power_of_x *= x;
        sum += power_of_x / factorial(i);
    }

    return sum;
}

int main() {
    double x;
    int terms;

    printf("Enter the value of x: ");
    scanf("%lf", &x);

    printf("Enter the number of terms to approximate e^x: ");
    scanf("%d", &terms);

    double result = compute_ex(x, terms);
    printf("Estimated value of e^%.2f using %d terms: %.10f\n", x, terms, result);

    return 0;
}
#endif
