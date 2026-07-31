#include <stdio.h>

void main () {
	int cows, legs;
	
	puts("How many cow legs did you count?");
	scanf("%d", &legs);
	
	cows = legs/4;
	
	printf("That implies there are %d cows.\n", cows);
}
