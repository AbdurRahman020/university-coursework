#include <stdio.h>
#include <math.h>

int main() {
	const double PI = 3.141592653;
	
	int A, f, p;
	float v, t;
	 
	printf("Enter A: ");
	scanf("%d", &A);
	
	printf("Enter f: ");
	scanf("%d", &f);
	
	printf("Enter t: ");
	scanf("%f", &t);
	
	printf("Enter p in degrees: ");
	scanf("%d", &p);
	
	float p_rad = p * PI / 180;

	v = A*sin(2 * PI * f * t + p_rad);
	
	printf("v = %lf\n", v);
	
	return 0;
}