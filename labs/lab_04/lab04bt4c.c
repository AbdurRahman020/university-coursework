#include <stdio.h>  

int main() {     
    int n = 5, i, j, mid = n / 2;

    for (i = 0; i <= mid; i++) {
        for (j = 0; j < i; j++)
            printf(" ");
        for (j = 0; j < 2 * (mid - i) + 1; j++)
            printf("*");
        printf("\n");
    }

    for (i = mid - 1; i >= 0; i--) {
        for (j = 0; j < i; j++)
            printf(" ");
        for (j = 0; j < 2 * (mid - i) + 1; j++)
            printf("*");
        printf("\n");
    }

    return 0; 
}
