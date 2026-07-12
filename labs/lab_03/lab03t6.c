#include <stdio.h>
#include <math.h>

int main() {
    float x;
    const float epsilon = 0.000001; 

    printf("Enter a floating point number: ");
    scanf("%f", &x);

    if (fabs(x - 0.1) < epsilon)
        puts("The value of x is 0.1");

    return 0;
}

