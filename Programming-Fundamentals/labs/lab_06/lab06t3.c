#include <stdio.h>

void transfer(int arr[], int argv[], int num_of_elements);
void print_array(int arr[], int num_of_elements);

int main() {
    int num_of_elements = 3;
    int arr[32], argv[32];
    
    for (int i = 0; i < num_of_elements; i++)
        scanf("%d", &argv[i + 1]);
    
    transfer(arr, argv, num_of_elements);
    print_array(arr, num_of_elements);

    return 0;
}

void transfer(int arr[], int argv[], int num_of_elements) {
    for (int i = 0; i < num_of_elements; i++)
        arr[i] = argv[i + 1];
}

void print_array(int arr[], int num_of_elements) {
    printf("The array elements are: ");
    
    for (int i = 0; i < num_of_elements; i++)
        printf("%d ", arr[i]);

    puts("");
}