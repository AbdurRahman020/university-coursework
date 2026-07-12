#include <stdio.h>

int main() {
    int n = 3, i, j;

    for (i = n - 1; i >= 0; i--) {
        for (j = 0; j < n - i; j++) {
            printf(" ");
        }
        for (j = 0; j < 2 * i + 1; j++) {
            printf("*");
        }
        printf("\n");
    }

    return 0;
}
