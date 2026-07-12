#include <stdio.h>

// function prototypes
void printMatrix(int r, int c, int arr[r][c]);
void transposeMatrix(int r, int c, int arr[r][c]);

int main() {
    int r, c;

    // get matrix dimensions from user
    printf("Enter number of rows: ");
    scanf("%d", &r);

    printf("Enter number of columns: ");
    scanf("%d", &c);

     // variable Length Array (VLA)
    int arr[r][c];

    // input matrix elements
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            printf("Enter element [%d][%d]: ", i, j);
            scanf("%d", &arr[i][j]);
        }
    } 

    // display original matrix
    printf("Original Matrix:\n");
    printMatrix(r, c, arr);

    // display transposed matrix
    printf("Transposed Matrix:\n");
    transposeMatrix(r, c, arr);

    return 0;
}

// prints a matrix in row-column format
void printMatrix(int r, int c, int arr[r][c]) {
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            printf("%d ", arr[i][j]);
        }
        puts(""); // move to next line after each row
    }
}

// prints the transpose of a matrix (swaps rows and columns)
void transposeMatrix(int r, int c, int arr[r][c]) {
    for (int i = 0; i < c; i++) {
        for (int j = 0; j < r; j++) {
            printf("%d ", arr[j][i]); 
        }
        puts("");
    }
}
