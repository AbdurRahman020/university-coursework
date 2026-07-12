#include <stdio.h>

int main() {
    int i = 1, k = 1;
    
    while (i<=5) {
        printf("%d", i);
        if (k==5)
            printf("lab04");
        i++;
        k+=2;
    }
    return 0;
}
