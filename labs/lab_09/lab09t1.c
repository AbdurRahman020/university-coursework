#include <stdio.h>
#include <stdlib.h>

int main() {
    int *arr = malloc(5 * sizeof(int));

    for (size_t i = 0; i < 5; i++) {
        arr[i] = (int)i;
        printf("arr[%zu] = %d\n", i, arr[i]);
    }

    free(arr);

    return 0;
}
