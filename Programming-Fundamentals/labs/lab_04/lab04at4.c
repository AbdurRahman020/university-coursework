#include <stdio.h>

int main() {
    int x = 1;
    
    while (x <= 5) {
        int y = 1;
        while (y <= 5) {
            printf("%s", "*");
            y++;
        }
        puts("");
        x++;
    }

    return 0;
}
