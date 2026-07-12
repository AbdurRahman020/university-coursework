#include <stdio.h>
#include <limits.h>

void minArray(int arr[], int arr_len) {
    int m = INT_MAX; 

    for (int i = 0; i < arr_len; i++) {
        if (arr[i] < m)
            m = arr[i];
    }
    printf("Min: %d\n", m);
}

void maxArray(int arr[], int arr_len) {
    int m = INT_MIN;

    for (int i = 0; i < arr_len; i++) {
        if (arr[i] > m)
            m = arr[i];
    }
    printf("Max: %d\n", m);
}

int main() {
    int a[6] = {5, 2, 3, 4, 22, 5};
    int arr_len = sizeof(a) / sizeof(a[0]);

    minArray(a, arr_len);
    maxArray(a, arr_len);

    return 0;
}
