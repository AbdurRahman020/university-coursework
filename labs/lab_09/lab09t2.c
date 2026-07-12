#include <stdio.h>
#include <stdlib.h>

int* foo(size_t);

int main() {
    size_t n = 5;
    int *arr = foo(n);

    if (arr == NULL) {
        fprintf(stderr, "Memory allocation failed!\n");
        return 1;
    }

    for (size_t i = 0; i < n; i++)
        *(arr + i) = (int)i;
    
    for (size_t i = 0; i < n; i++)
        printf("*(arr + %zu) = %d\n", i, *(arr + i));

    free(arr);

    return 0;
}

int* foo(size_t n) {
    int *j = malloc(n * sizeof(int));

    if (j == NULL)
        fprintf(stderr, "Memory allocation failed inside foo().\n");

    return j;
}
