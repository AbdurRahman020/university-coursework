#include<stdio.h>

// function prototypes
void function1(int);
void function2(int);
void function3(int);

int main() {
	/* initialize array of 3 pointers to function that each take
	   an int argument and return void */
	void (*f[3])(int) = {function1, function2, function3};
	
	size_t choice;
	
	printf("Enter a number between 0 and 2, and 3 to end: ");
	scanf("%d", &choice);
	
	while (choice >= 0 && choice < 3) {
		/* invoke function at loaction choice in array f and pass
		   choice as an argument */
		(*f[choice])(choice);
		
		printf("Enter a number between 0 and 2, and 3 to end: ");
		scanf("%d", &choice);
	}
	puts("Program execution completed.");

	return 0;
}

void function1(int a) {
	printf("You entered %d so function1 was called.\n\n", a);
}

void function2(int b) {
	printf("You entered %d so function2 was called.\n\n", b);
}

void function3(int c) {
	printf("You entered %d so function3 was called.\n\n", c);
}
