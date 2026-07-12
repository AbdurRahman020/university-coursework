#include <stdio.h>

int main() {
    int rows = 6, columns = 8;

    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < columns; j++) {
            if ((i + j) % 2 == 0)
                printf("* ");
            else
                printf("  ");  
        }
        puts("");
    }

    return 0;
}
