#include <stdio.h>
#include <math.h>

struct point {
    int x, y;
};

int main() {
    struct point p1, p2;
    struct point *j = &p1;
    struct point *k = &p2;

    // initialize points using pointers
    j->x = 0, j->y = 0;
    k->x = 3, k->y = 4;

    int dx = k->x - j->x;
    int dy = k->y - j->y;

    double distance = sqrt(dx*dx + dy*dy);

    printf("Distance between points: %.2f\n", distance);

    return 0;
}
