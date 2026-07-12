#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

// function prototypes
void printArray(int arr[], int size);
void swap(int *a, int *b);
void bubblesort(int arr[], int size);
void decimalToBinary(int arr[], int size);
bool isBinaryPalindrome(int num);
int palindromeCounter(int arr[], int size);

int main() {
    int mockarray[10] = {123, 45, 212, 89, 77, 56, 33, 101, 256, 11};

    // display original array
    printf("Original Array:\n");
    printArray(mockarray, 10);

    // sort array with custom logic (descending first half, ascending second half)
    bubblesort(mockarray, 10);

    // display sorted array
    printf("Sorted Array: ");
    printArray(mockarray, 10);

    // convert and display binary representations
    decimalToBinary(mockarray, 10);

    // count and display numbers with palindromic binary representations
    int count = palindromeCounter(mockarray, 10);
    printf("\nPalindrome Binary Count: %d\n", count);

    return 0;
}

// prints all elements of an array
void printArray(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    puts("");
}

// swaps two integers using pointers
void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

// custom bubble sort: sorts first 5 elements descending, last 5 ascending
void bubblesort(int arr[], int size) {
    // sort first 5 elements in descending order
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4 - i; j++) {
            if (arr[j] < arr[j + 1]) {
                swap(&arr[j], &arr[j + 1]);
            }
        }
    }

    // sort last 5 elements in ascending order
    for (int i = 5; i < size - 1; i++) {
        for (int j = 5; j < size - (i - 4) - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(&arr[j], &arr[j + 1]);
            }
        }
    }
}

// converts decimal numbers to binary and prints them
void decimalToBinary(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        int num = arr[i];
        int bin[32], index = 0; // binary digits stored in reverse

        // handle zero case
        if (num == 0) {
            printf("Binary of %d: 0\n", num);
            continue;
        }

        // convert decimal to binary (stores in reverse order)
        while (num > 0) {
            bin[index++] = num % 2;
            num /= 2;
        }

        printf("Binary of %d: ", arr[i]);
        
        // print binary digits in correct order (reverse)
        for (int j = index - 1; j >= 0; j--) {
            printf("%d", bin[j]);
        }

        puts("");
    }
}

// checks if a number's binary representation is a palindrome
bool isBinaryPalindrome(int num) {
    int bin[32], index = 0;

    // zero is considered a palindrome
    if (num == 0)
        return true;

    // convert decimal to binary (stored in reverse)
    while (num > 0) {
        bin[index++] = num % 2;
        num /= 2;
    }

    // check if binary representation is palindrome using two pointers
    for (int i = 0, j = index - 1; i < j; i++, j--) {
        if (bin[i] != bin[j]) {
            return false;
        }
    }

    return true;
}

// counts how many numbers in array have palindromic binary representations
int palindromeCounter(int arr[], int size) {
    int count = 0;

    for (int i = 0; i < size; i++) {
        if (isBinaryPalindrome(arr[i])) {
            count++;
        }
    }

    return count;
}
