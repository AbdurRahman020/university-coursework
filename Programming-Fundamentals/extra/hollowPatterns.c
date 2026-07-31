#include <stdio.h>

void printHollowDiamond(int);
void printHollowSquare(int);
void printHollowTriangle(int);

int main() {
    int choice, n;

    while(1) {
        printf("\nSelect the shape to print:\n");
        printf("1. Hollow Diamond\n");
        printf("2. Hollow Square\n");
        printf("3. Hollow Triangle\n");
        printf("-1 to Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        if(choice == -1) {
            printf("Exiting the program.\n");
            break;
        }

        // get the size for the shape
        if (choice == 1) {
            printf("Enter the size of the hollow diamond: ");
            scanf("%d", &n);
            printHollowDiamond(n);
        } else if (choice == 2) {
            printf("Enter the size of the hollow square: ");
            scanf("%d", &n);
            printHollowSquare(n);
        } else if (choice == 3) {
            printf("Enter the number of rows for the hollow triangle: ");
            scanf("%d", &n);
            printHollowTriangle(n);
        } else {
            printf("Invalid choice. Please try again.\n");
        }
    }

    return 0;
}

void printHollowDiamond(int n) {
    int i, j;

    // upper half of the diamond
    for(i = 0; i < n; i++) {
        for(j = 0; j < 2*n - 1; j++) {
            if(j == n - i - 1 || j == n + i - 1)
                printf("*");
            else
                printf(" ");
        }
        puts("");
    }

    // lower half of the diamond
    for(i = n - 2; i >= 0; i--) {
        for(j = 0; j < 2*n - 1; j++) {
            if(j == n - i - 1 || j == n + i - 1)
                printf("*");
            else
                printf(" ");
        }
        puts("");
    }
}

void printHollowSquare(int n) {
    int i, j;

    for(i = 0; i < n; i++) {
        for(j = 0; j < n; j++) {
            // print '*' on the borders of the square
            if(i == 0 || i == n - 1 || j == 0 || j == n - 1)
                printf("*");
            else
                printf(" ");
        }
        puts("");
    }
}

void printHollowTriangle(int n) {
    int i, j;

    for(i = 0; i < n; i++) {
        for(j = 0; j <= i; j++) {
            // print '*' on the borders and first and last row
            if (j == 0 || j == i || i == n - 1)
                printf("*");
            else
                printf(" ");
        }
        puts("");
    }
}
