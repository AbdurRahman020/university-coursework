#include <stdio.h>

int main() {
    int x, t, y, i, j, count = 0;

    // get base value from user
    printf("Input the value of x: ");
    scanf("%d", &x);
    
    // get number of terms in the series
    printf("Input number of terms: ");
    scanf("%d", &t);

    // generate series: -x - x^3 + x^5 - x^7 + x^9 - ...
    for (i = 0; i < t; i++) {
         // start with base value
        y = x;

        // calculate odd power: x^(2i+1) = x^1, x^3, x^5, x^7, ...
        for (j = 1; j < 2*i + 1; j++)
            y = y * x;

        // alternate signs: negative for even i, positive for odd i
        if (i % 2 == 0) {
             // make term negative
            y = -y;
            printf("%d\n", y);
        } else {
            // keep term positive
            printf("%d\n", y);
        }
        
        // add current term to running sum
        count += y; 
    }
     
    // display final sum of all terms
    printf("The sum = %d\n", count);
    
    return 0;
}