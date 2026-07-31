#include <stdio.h>

int main() {
    char x, y;

    printf("Enter x: ");
    x = getchar();

    getchar();
    
    printf("Enter y: ");
    y = getchar();

    if ((x == 't' || x == 'f') && (y == 't' || y == 'f')) {
        if (x == 't' && y == 't')
            printf("%c AND %c is TRUE\n", x, y);
        else
            printf("%c AND %c is FALSE\n", x, y);
    } else 
        printf("Invalid input!\n");

    return 0;
}
