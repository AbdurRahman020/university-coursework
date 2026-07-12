#include <stdio.h>

void swap(int[], int, int);
void print_array(int[], int);

int main() {
    int a[9] = {5, 9, -2, 150, -95, 23, 2, 5, 80};

    swap(a, 3, 5);
    print_array(a, 9);

    return 0;
}

void swap(int a[], int i, int j) {
    int temp = a[i];
    a[i] = a[j];
    a[j] = temp;
}

void print_array(int a[], int n) {
    for (int i = 0; i < n; i++)
        printf("%d ", a[i]);
    puts("");
}
