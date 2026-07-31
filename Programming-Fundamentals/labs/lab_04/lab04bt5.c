#include <stdio.h>

int main() {
    int pass, f, x;
    
    printf("Have you passed FSc Exams? (Y/N): ");
    pass = getchar();

    if (pass == 'Y') {
        printf("FSc marks?: ");
        scanf("%d", &f);

        printf("Entry Test Marks?: ");
        scanf("%d", &x);
        
        float prcntge = f / 1100.0 * 100; 
        printf("Your percentage is: %f\n", prcntge);
        
        if (x > 80 && f > 900)
            puts("You are admitted to EE Dept");
        else
            puts("Sorry you can't be admitted to EE Dept");
    }
    else
        puts("Program ends here");

}
