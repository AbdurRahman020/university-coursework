#include <stdio.h>
#include <math.h>

// #define DistanceFormula  
// #define QuadraticEqRoots
#define NumberReverse
// #define IsPrime
// #define TriangleType


#ifdef DistanceFormula
float distance (int x1, int y1, int x2, int y2) {
	float x, y, d;
	
	x = x2 - x1;
	y = y2 - y1;
	d = sqrt(pow(x, 2)+ pow(y, 2));

	return d;
}

int main() {
	int x1, x2, y1, y2;
	float d;

	printf("Enter the coordinates of first point: ");
	scanf("%d %d",&x1,&y1);
	printf("Enter the coordinates of second point: ");
	scanf("%d %d",&x2,&y2);
	
	d = distance(x1, y1, x2, y2); 
	printf("Distance between the ponits is: %.2f", d);	

    return 0;
}
#endif


#ifdef QuadraticEqRoots
int main() {
    float a, b, c, determinant, r1, r2, real, imag;
    
	printf("Enter coefficients a, b and c:");
    scanf("%f%f%f", &a, &b, &c);
    
    determinant == b*b - 4*a*c; 

    if (determinant > 0) {
        r1 = (-b + sqrt(determinant))/2*a;
        r2 = (-b - sqrt(determinant))/2*a;

        printf("\nRoots are: %.2f and %.2f ", r1, r2);
    } else if (determinant == 0) { 
        r1 = r2 = -b/(2*a);
        printf("\nRoots are: %.2f and %.2f ", r1, r2);
    } else {
        real = -b/(2*a);
        imag = sqrt(-determinant)/(2*a);
        printf("\n\nRoots are %.2f + i%.2f and %.2f - i%.2f ", real, imag, real, imag);
    }

    return 0;
}
#endif


#ifdef NumberReverse
int main() {
  int n, reverse = 0, remainder;

  printf("Enter an integer: ");
  scanf("%d", &n);

  while (n != 0) {
    remainder = n % 10;
    reverse = reverse * 10 + remainder;
    n /= 10;
  }

  printf("Reversed number = %d", reverse);

  return 0;
}
#endif


#ifdef IsPrime
int main() {
	int num, i;
	
	puts("Prime Numbers Checking");
	printf("Enter the number to check: ");
	scanf("%d",&num);
	
	if (num == 0 || num == 1) {
		printf("Number is not Prime.");
	} else {
		for(i=2; i <= num/2; i++) {
			if (num%i == 0)
				printf("Number is not prime");
			else
				printf("Number is prime");
			break;
		}
	}

    return 0;
}
#endif


#ifdef TriangleType
int isValidTriangle(int *sides) {
    return (sides[0] + sides[1] > sides[2]) && 
           (sides[1] + sides[2] > sides[0]) && 
           (sides[0] + sides[2] > sides[1]);
}

void determineTriangleType(int *sides) {
    if (!isValidTriangle(sides)) {
        puts("Not a valid triangle");
        return;
    }

    if (sides[0] == sides[1] && sides[1] == sides[2])
        puts("Equilateral triangle");
    else if (sides[0] == sides[1] || sides[1] == sides[2] || sides[0] == sides[2])
        puts("Isosceles triangle");
    else
        puts("Scalene triangle");
}

int main() {
    int sides[3];

    puts("Enter the three sides of the triangle: ");
    for (int i = 0; i < 3; i++) {
        printf("Side %d: ", i + 1);
        scanf("%d", &sides[i]);
    }

    determineTriangleType(sides);

    return 0;
}
#endif
