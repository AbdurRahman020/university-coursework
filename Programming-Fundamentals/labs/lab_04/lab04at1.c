#include <stdio.h>

int main(void) {
	int x;

	printf("1234567890123456789123\n");
	printf("%s%s%s\n", "Integer", "Square", "Cube");

	for(x = 1; x <= 5; x++) {
		printf("%d%d%d\n", x, x*x, x*x*x);
	}

	return 0;
}
