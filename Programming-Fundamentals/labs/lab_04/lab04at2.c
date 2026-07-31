#include <stdio.h>

int main() {

    int x = 5;
    while (x >= 1) {
        printf("%d book(s) are on the shelf.\n", x);

        if (x != 1)
            printf("Take one book down, pass it around, %d book(s) are left.\n", x - 1);
        else
            puts("Take one down, pass it around, no more books.");

        x--;
    }

    return 0;
}
