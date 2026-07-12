#include <stdio.h>

void transfer(int arr[], int argv[], int num_of_elements);
void swap(int a[], int i, int j);
void BubbleSort(int x[], int n);
void print_array(int arr[], int num_of_elements);

int main() {
    int num_of_elements = 9;
    int arr[32], argv[32] = {0};
    
    for (int i = 0; i < num_of_elements; i++)
        scanf("%d", &argv[i + 1]);
    
    transfer(arr, argv, num_of_elements);
    BubbleSort(arr, num_of_elements);
    print_array(arr, num_of_elements);

    return 0;
}

void transfer(int arr[], int argv[], int num_of_elements) {
    for (int i = 0; i < num_of_elements; i++)
        arr[i] = argv[i + 1];
}

void swap(int a[], int i, int j) {
    int temp = a[i];
    a[i] = a[j];
    a[j] = temp;
}

void BubbleSort(int x[], int n) {
    int s;
    do {
        s = 0;
        for (int i = 1; i < n; i++) {
            if (x[i-1] > x[i]) {
                swap(x, i, i-1);
                s = 1;
            }
        }
    } while (s != 0);
}

void print_array(int arr[], int num_of_elements) {
    printf("The array elements are: ");
    
    for (int i = 0; i < num_of_elements; i++)
        printf("%d ", arr[i]);

    puts("");
}
