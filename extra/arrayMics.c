#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void initializeArray(int arr[], size_t size);
void printArray(int arr[], size_t size);
int sumArray(int arr[], size_t size);
void findMinMax(int arr[], size_t size, int *min, int *max);
void sortArray(int arr[], size_t size);
int countEven(int arr[], size_t size);

int main() {
    int arr[10];
    int min, max;

    srand(time(0));
    
    initializeArray(arr, 10);
    printArray(arr, 10);
    
    printf("Sum: %d\n", sumArray(arr, 10));
    findMinMax(arr, 10, &min, &max);
    
    printf("Min: %d, Max: %d\n", min, max);
    sortArray(arr, 10);

    printf("Sorted array: ");
    printArray(arr, 10);
    
    printf("Even count: %d\n", countEven(arr, 10));

    return 0;
}

void initializeArray(int arr[], size_t size) {
    for (size_t i = 0; i < size; i++)
        *(arr + i) = rand() % 100 + 1;
}

void printArray(int arr[], size_t size) {
    for (size_t i = 0; i < size; i++)
        printf("%d ", *(arr + i));
    puts("");
}

int sumArray(int arr[], size_t size) {
    int sum = 0;
    
    for (size_t i = 0; i < size; i++)
        sum += *(arr + i);
    
    return sum;
}

void findMinMax(int arr[], size_t size, int *min, int *max) {
    *min = *max = *arr;

    for (size_t i = 1; i < size; i++) {
        if (*(arr + i) < *min)
            *min = *(arr + i);
        if (*(arr + i) > *max)
            *max = *(arr + i);
    }
}

void sortArray(int arr[], size_t size) {
    for (size_t i = 0; i < size - 1; i++) {
        for (size_t j = i + 1; j < size; j++) {
            if (*(arr + i) > *(arr + j)) {
                int temp = *(arr + i);
                *(arr + i) = *(arr + j);
                *(arr + j) = temp;
            }
        }
    }
}

int countEven(int arr[], size_t size) {
    int count = 0;

    for (size_t i = 0; i < size; i++) {
        if (*(arr + i) % 2 == 0)
            count++;
    }

    return count;
}
