#include <stdio.h>

int main (void) {
	float age;
	
	printf("Enter your age: ");
	scanf("%f", &age);
	
	if (age >= 18)
		puts("You are eligible for the driving license.\n");
	else
		puts("You're not eligible for the driving license.\n");
	
	return 0;
}
