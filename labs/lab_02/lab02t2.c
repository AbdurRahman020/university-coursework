#include <stdio.h>

int main() {
	int a, b, c, sum_ints, mul_ints;
	float avg;
	
	printf("Input three integers: ");
	
	scanf("%d%d%d", &a, &b, &c);
	
	sum_ints = a + b + c;
	mul_ints = a * b * c;
	
	avg = sum_ints/3.0;
	
	printf("The sum is %d\n", sum_ints);
	printf("The product is %d\n", mul_ints);
	printf("The average is %f\n", avg);
	
	return 0;
}
