#include <stdio.h>
#include <math.h>

struct point {
    int x, y;
};

void foo(struct point *, struct point *, double *);

int main() {
    struct point p1 = {0, 0};
    struct point p2 = {3, 4};
    
    struct point *j = &p1;
    struct point *k = &p2;

    double dist;
    
    foo(j, k, &dist);

    printf("Distance between points: %.2f\n", dist);

    return 0;
}

// function to calculate distance using pointers
void foo(struct point *j, struct point *k, double *a) {
    int dx = k->x - j->x;
    int dy = k->y - j->y;
    
    *a = sqrt(dx * dx + dy * dy);
}
