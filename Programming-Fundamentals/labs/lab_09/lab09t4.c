#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(int argc, char *argv[]) {
    if (argc < 2) {
        fprintf(stderr, "Usage: %s <num_chars>\n", argv[0]);
        return 1;
    }

    int n = atoi(argv[1]);  // number of characters in the pattern
    if (n <= 0) {
        fprintf(stderr, "Please provide a positive number.\n");
        return 1;
    }

    // dynamically allocate memory for the pattern array
    char *pattern = (char*)malloc(n * sizeof(char));
    if (pattern == NULL) {
        fprintf(stderr, "Memory allocation failed!\n");
        return 1;
    }

    // seed the random number generator
    srand(time(NULL));

    for (int i = 0; i < n; i++) {
        pattern[i] = (rand() % 2) ? '*' : '.';  // randomly choose '*' or '.'
    }

    printf("Generated Pattern:\n");
    for (int i = 0; i < n; i++) {
        printf("%c", pattern[i]);
    }

    printf("\n");

    free(pattern);

    return 0;
}
