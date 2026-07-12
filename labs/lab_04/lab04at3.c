#include <stdio.h>
#include <string.h> 

float getGradePoint(char grade[]);

int main() {
    int num_of_subjects;
    float total_grade_points = 0.0, total_credits = 0.0;
    
    printf("Enter the number of subjects: ");
    scanf("%d", &num_of_subjects);

    for (int i = 0; i < num_of_subjects; i++) {
        char grade[3];  
        int credit_hours;
        
        printf("Enter credit hours and grade for subject %d: ", i + 1);
        scanf("%d %2s", &credit_hours, grade);
        
        float grade_points = getGradePoint(grade);

        if (grade_points == -1) {
            printf("Invalid grade entered, exiting the program.\n");
            return 1;
        }

        total_grade_points += grade_points * credit_hours;
        total_credits += credit_hours;
    }
    
    if (total_credits > 0) {
        float GPA = total_grade_points / total_credits;
        printf("GPA = %.2f\n", GPA);
    } else {
        printf("Error: Total credits cannot be zero.\n");
    }

    return 0;
}

float getGradePoint(char grade[]) {
    if (strcmp(grade, "A+") == 0)
        return 4.0;
    else if (strcmp(grade, "A") == 0)
        return 4.0;
    else if (strcmp(grade, "A-") == 0) 
        return 3.7;
    else if (strcmp(grade, "B+") == 0) 
        return 3.3;
    else if (strcmp(grade, "B") == 0) 
        return 3.0;
    else if (strcmp(grade, "B-") == 0) 
        return 2.7;
    else if (strcmp(grade, "C+") == 0)
        return 2.3;
    else if (strcmp(grade, "C") == 0)
        return 2.0;
    else if (strcmp(grade, "C-") == 0)
        return 1.7;
    else if (strcmp(grade, "D+") == 0)
        return 1.3;    
    else if (strcmp(grade, "D") == 0)
        return 1.0;
    else if (strcmp(grade, "F") == 0)
        return 0.0;
    else {
        printf("Invalid grade input.\n");
        return -1;
    }
}
