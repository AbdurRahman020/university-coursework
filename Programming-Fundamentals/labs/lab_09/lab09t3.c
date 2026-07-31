#include <stdio.h>
#include <stdlib.h>

int* foo(size_t);

int main(int argc, char *argv[]) {
    if (argc < 2) {
        fprintf(stderr, "Usage: %s <num_elements> <element1> <element2> ...\n", argv[0]);
        return 1;
    }

    size_t n = (size_t)atoi(argv[1]); // max number of elements
    if ((size_t)(argc - 2) < n) {
        fprintf(stderr, "Not enough elements provided.\n");
        return 1;
    }

    int *x = foo(n);

    if (x == NULL)
        return 1;
    
    for (size_t i = 0; i < n; i++)
        *(x + i) = atoi(argv[i + 2]);
    
    printf("Array elements:\n");
    for (size_t i = 0; i < n; i++)
        printf("%d\n", *(x + i));

    free(x);
    
    return 0;
}

int* foo(size_t n) {
    int *ptr = (int*)calloc(n, sizeof(int));
    
    if (ptr == NULL)
        fprintf(stderr, "Memory allocation failed!\n");
    
    return ptr;
}
