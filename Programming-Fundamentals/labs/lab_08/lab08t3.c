#include <stdio.h>

int main() {
    int x[5] = {1, 2, 3, 4, 5}, y[5] = {1, 2, 3, 4, 5}, z[5]; 
    
    for (size_t i = 0; i < 5; i++)
        *(z + i) = *(x + i) + *(y + i);
    
    
    printf("z[5] = {");
    
    for (size_t i = 0; i < 5; i++) {
        printf("%d", *(z + i));
        if (i < 4)
            printf(", "); 
    }
    
    printf("}\n");

    return 0;
}
