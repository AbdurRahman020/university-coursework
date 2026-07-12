#include <stdio.h>

int main() {
    int num_rows, curr_row, space, star;

    printf("Enter no. of rows of the diamond: ");
    scanf("%d", &num_rows);

    for (curr_row = num_rows/2; curr_row >=0; curr_row--) {
        for (space = 0; space < num_rows/2 - curr_row; space++)
            printf(" ");
        for (star = 0; star < 2*curr_row + 1; star++)
            printf("*");
        puts("");
    }
    
    for (curr_row = 0; curr_row < num_rows/2; curr_row++) {
        for (space = 0; space < num_rows/2 - curr_row - 1; space++)
            printf(" ");
        for (star = 0; star < 2*curr_row + 3; star++)
            printf("*");
        puts("");
    }

    return 0; 
}
