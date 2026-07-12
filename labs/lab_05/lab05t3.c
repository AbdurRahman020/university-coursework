#include <stdio.h>
#include <math.h>

int PrintDay(int, int, int);

int main() {
    int q, m, y;

    printf("Enter date: ");
    scanf("%d%d%d", &q, &m, &y);

    printf("The day is: ");
    PrintDay(q, m, y);

    return 0;
}

int PrintDay(int q, int m, int y) {
    int h, j, k;

    if (m == 1 || m == 2) {
        m += 12;
        y -= 1;
    }

    h = (q + (13 * (m + 1)) / 5 + y + y / 4 - y / 100 + y / 400) % 7;

    switch (h) {
        case 0:
            printf("Saturday\n");
            break;
        case 1:
            printf("Sunday\n");
            break;
        case 2:
            printf("Monday\n");
            break;
        case 3:
            printf("Tuesday\n");
            break;
        case 4:
            printf("Wednesday\n");
            break;
        case 5:
            printf("Thursday\n");
            break;
        case 6:
            printf("Friday\n");
            break;
    }

    return 0;
}
