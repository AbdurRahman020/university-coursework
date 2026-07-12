#include <stdio.h>
#include <stdlib.h>

// allocates memory for an array of n integers
int* foo(int n) {
    int *j = malloc(n * sizeof(int));
    if (j == NULL) {
        fprintf(stderr, "Unable to allocate memory\n");
        exit(1);
    }
    return j;
}

// swaps the contents of two arrays
void swapArray(int arr1[], int arr2[], int size) {
    int arr_temp[size];
    for (int i = 0; i < size; i++) {
        arr_temp[i] = arr1[i];
        arr1[i] = arr2[i];
        arr2[i] = arr_temp[i];
    }
}

// prints all elements of an array
void printArray(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    puts("");
}

int main() {
    int n;

    printf("Enter the number of elements: ");
    scanf("%d", &n);

    // dynamically allocate memory for both arrays
    int *arr1 = foo(n);
    int *arr2 = foo(n);

    // input elements for first array
    for (int i = 0; i < n; i++) {
        printf("Enter Array1[%d]: ", i);
        scanf("%d", &arr1[i]);
    }

    // input elements for second array
    for (int i = 0; i < n; i++) {
        printf("Enter Array2[%d]: ", i);
        scanf("%d", &arr2[i]);
    }

    // display arrays before swap
    printf("Before swap:\n");
    printf("Array1: ");
    printArray(arr1, n);
    printf("Array2: ");
    printArray(arr2, n);

    // swap the arrays
    swapArray(arr1, arr2, n);

    // display arrays after swap
    printf("After swap:\n");
    printf("Array1: ");
    printArray(arr1, n);
    printf("Array2: ");
    printArray(arr2, n);

    // free dynamically allocated memory
    free(arr1);
    free(arr2);

    return 0;
}