#include <stdio.h>

int main() {
    int x[5] = {1, 2, 3, 4, 5};
	
    int i;
	printf("1234567890123456789012\n");
	printf("%7s%8s%12s\n","Element","Value","Address");
	
    for(i = 0; i < 5; i++){
		printf("%2sx[%d]%7d%21p\n", "", i, x[i], &x[i]);
	}

    return 0;
}
