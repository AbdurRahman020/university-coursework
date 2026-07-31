#include <stdio.h>

int main() {
    int x[5] = {1, 2, 3, 4, 5};
    int sum = 0;
	
    for (int i = 0; i < 5; i++)
        sum += *(x+i);
	
    
	printf("The sum is: %d\n", sum);

    return 0;
}
