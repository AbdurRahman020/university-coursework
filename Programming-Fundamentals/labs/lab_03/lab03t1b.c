#include <stdio.h>

int main () {
    char flag;
    float age;

    printf("Do you want to proceed? Eneter y for yes and n for no: ");
    scanf(" %c", &flag);
    
    if (flag == 'y') {
        printf("Enter your age: ");
        scanf("%f", &age);
        
        if (age >= 18)
            printf("You are eligible for the driving license.\n");
        else
            printf("You're not eligible for the driving license.\n");
    }
    else if (flag == 'n')
        printf("End of the program.\n");
    else
        printf("Invalid Input\n");

    return 0;
}
