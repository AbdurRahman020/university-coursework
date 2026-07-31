#include <stdio.h>
#include <math.h>

struct point {
    int x, y;
};

double foo(struct point p1, struct point p2);


int main() {
    struct point p1 = {0, 0};
    struct point p2 = {3, 4};

    double distance = foo(p1, p2);

    printf("Distance between points: %.2f\n", distance);

    return 0;
}

// function to calculate distance between two points
double foo(struct point p1, struct point p2) {
    int dx = p2.x - p1.x;
    int dy = p2.y - p1.y;
    
    return sqrt(dx * dx + dy * dy);
}
