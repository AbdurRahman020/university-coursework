#include <stdio.h>

#define SIZE 20

// function to copy string using array indexing
void arrayIndex(char arrToBeCopied[], char arrCopy[]) {
    for (size_t i = 0; i < SIZE; i++) {
        arrCopy[i] = arrToBeCopied[i];
    }
}

// function to copy string using pointer dereferencing
void pointerDref(char *arrToBeCopied, char *arrCopy) {
    for (size_t i = 0; i < SIZE; i++) {
        *(arrCopy + i) = *(arrToBeCopied + i);
    }
}

// function to copy string using pointer arithmetic
void pointerArth(char arrToBeCopied[], char arrCopy[]) {
    char *p = arrToBeCopied;
    for (size_t i = 0; i < SIZE; i++) {
        *(arrCopy + i) = *(p + i);
    }
}

int main() {
    char arrCopied[SIZE] = {0};
    char arr[] = "Hello! How are you?";

    int choice;
    
    printf("Choose a string copying method:\n");
    printf("1. Array Indexing\n");
    printf("2. Pointer Dereferencing\n");
    printf("3. Pointer Arithmetic\n");
    printf("Enter Choice (1-3): ");
    scanf("%d", &choice);

    switch (choice) {
        case 1:
            arrayIndex(arr, arrCopied);
            break;
        case 2:
            pointerDref(arr, arrCopied);
            break;
        case 3:
            pointerArth(arr, arrCopied);
            break;
        default:
            printf("Wrong Choice!\n");
            return 1;
    }

    printf("Copied String: %s\n", arrCopied);

    return 0;
}
