#include <stdio.h>
#include <math.h>

struct point {
    int x, y;
};

int main() {
    struct point p1 = {0, 0};
    struct point p2 = {3, 4};

    int dx = p2.x - p1.x;
    int dy = p2.y - p1.y;

    double distance = sqrt(dx*dx + dy*dy);

    printf("Distance between the points: %.2f\n", distance);

    return 0;
}
