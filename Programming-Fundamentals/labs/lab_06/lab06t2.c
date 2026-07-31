#include <stdio.h>

void sort(int[], int);
void print_array(int[], int);

int main() {
    int a[9] = {5, 9, -2, 150, -95, 23, 2, 5, 80};
    
    sort(a, 9);
    print_array(a, 9);
    return 0;
}

void sort(int a[], int n) {
    for (int i = 0; i < n - 1; i++)
        for (int j = i + 1; j < n; j++)
            if (a[i] > a[j]) {
                int temp = a[i];
                a[i] = a[j];
                a[j] = temp;
            }
}

void print_array(int a[], int n) {
    
    printf("The array elements after sorting are: ");
    
    for (int i = 0; i < n; i++)
        printf("%d ", a[i]);
    
    puts("");
}
