#include <stdio.h>
#include <string.h>

#define SIZE 50

int main() {
    char letArr[SIZE][3];
    int CrdArr[SIZE] = {0};
    float creditScore[SIZE] = {0};

    int numOfSub;
    float sumOfCreditHours = 0, sumOfCreditScore = 0, gpa = 0;

    printf("Enter number of subjects (maximum 50): ");
    scanf("%d", &numOfSub);
    
    if (numOfSub > SIZE || numOfSub <= 0) {
        printf("Invalid number of subjects!\n");
        return 1;
    }

    printf("\nEnter grades in order (e.g., A+, B, C-):\n"); 
    for (int i = 0; i < numOfSub; i++) {
        printf("Subject %d grade: ", i + 1);
        scanf("%s", letArr[i]);
    }

    printf("\nEnter credit hours for each subject:\n"); 
    for (int j = 0; j < numOfSub; j++) {
        printf("Subject %d credit hours: ", j + 1);
        scanf("%d", &CrdArr[j]);
    }

    // calculate credit score for each subject
    for (int k = 0; k < numOfSub; k++) {
        float gradePoint = 0.0;
        
        if (strcmp(letArr[k], "A+") == 0 || strcmp(letArr[k], "A") == 0) {
            gradePoint = 4.0;
        } else if (strcmp(letArr[k], "A-") == 0) {
            gradePoint = 3.7;
        } else if (strcmp(letArr[k], "B+") == 0) {
            gradePoint = 3.3;
        } else if (strcmp(letArr[k], "B") == 0) {
            gradePoint = 3.0;
        } else if (strcmp(letArr[k], "B-") == 0) {
            gradePoint = 2.7;
        } else if (strcmp(letArr[k], "C+") == 0) {
            gradePoint = 2.3;
        } else if (strcmp(letArr[k], "C") == 0) {
            gradePoint = 2.0;
        } else if (strcmp(letArr[k], "C-") == 0) {
            gradePoint = 1.7;
        } else if (strcmp(letArr[k], "D+") == 0) {
            gradePoint = 1.3;
        } else if (strcmp(letArr[k], "D") == 0) {
            gradePoint = 1.0;
        } else if (strcmp(letArr[k], "F") == 0) {
            gradePoint = 0.0;
        } else {
            printf("Invalid grade entered: %s\n", letArr[k]);
            return 1;
        }

        // Store credit score (grade point × credit hours) in third array
        creditScore[k] = gradePoint * CrdArr[k];
        sumOfCreditScore += creditScore[k];
    }

    // calculate cumulative credit hours
    for (int m = 0; m < numOfSub; m++) {
        sumOfCreditHours += CrdArr[m];
    }

    // calculate CGPA
    gpa = sumOfCreditScore / sumOfCreditHours;

    printf("\n=== GPA Calculation Results ===\n");
    printf("Total Credit Hours: %.0f\n", sumOfCreditHours);
    printf("Total Credit Score: %.2f\n", sumOfCreditScore);
    printf("Cumulative GPA (CGPA): %.2f\n", gpa);

    return 0;
}