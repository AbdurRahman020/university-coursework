#include <stdio.h>

int main() {
    int i = 0, j = 0;

    for (i = 1; i < 3; i++) {
        for (j = 1; j < 6; j++)
            printf("%d x %d = %d\n", i, j, i*j);
        puts("");
    }
    return 0;
}
