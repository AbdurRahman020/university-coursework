#include <stdio.h>

int main() {
    int r;
    printf("Enter the number of rows: ");
    scanf("%d", &r);

    // upper half of the pattern (including middle)
    for (int i = 0; i < r / 2 + 1; i++) {
        // print leading spaces
        for (int j = 0; j < i; j++)
            printf(" ");

        // print left hollow triangle (only border stars)
        for (int j = 0; j < r - 2 * i; j++)
            if (j == 0 || j == r - 2 * i - 1 || i == 0) {
                printf("*");
            } else {
                printf(" ");
            }

        // print middle gap spaces
        for (int j = 0; j < 2 * i; j++)
            printf(" ");
        
        // print right solid triangle
        for (int j = 0; j < r - 2 * i; j++)
            printf("*");
        
        puts("");
    }

    // lower half of the pattern (mirror of upper half)
    for (int i = r / 2 - 1; i >= 0; i--) {
        // print leading spaces
        for (int j = 0; j < i; j++)
            printf(" ");
        
        // print left solid triangle
        for (int j = 0; j < r - 2 * i; j++)
            printf("*");
        
        // print middle gap spaces
        for (int j = 0; j < 2 * i; j++)
            printf(" ");
        
        // print right hollow triangle (only border stars)
        for (int j = 0; j < r - 2 * i; j++)
            if (j == 0 || j == r - 2 * i - 1 || i == 0) {
                printf("*");
            } else {
                printf(" ");
            }
        
        puts("");
    }

    return 0;
}
