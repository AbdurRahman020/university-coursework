#include <stdio.h>

int main() {
    int n, i, j;

    printf("Enter the number of rows (odd number): ");
    scanf("%d", &n);

    if (n % 2 == 0) {
        printf("Please enter an odd number.\n");
        return 1;
    }

    int mid = n / 2;

    // upper part of the diamond
    for (i = 0; i <= mid; i++) {
        for (j = 0; j < mid - i; j++) {
            printf(" ");
        }
        for (j = 0; j < 2 * i + 1; j++) {
            printf("*");
        }
        printf("\n");
    }

    // lower part of the diamond
    for (i = mid - 1; i >= 0; i--) {
        for (j = 0; j < mid - i; j++) {
            printf(" ");
        }
        for (j = 0; j < 2 * i + 1; j++) {
            printf("*");
        }
        printf("\n");
    }

    return 0;
}
