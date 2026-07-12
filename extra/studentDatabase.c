#include <stdio.h>
#include <string.h>

#define MAX 50

struct Student {
    int roll;
    char name[50];
    float marks;
};

void addStudent(struct Student students[], int *count);
void displayStudents(struct Student students[], int count);

int main() {
    struct Student students[MAX];
    int count = 0, choice;

    do {
        printf("1. Add Student\n2. Display Students\n3. Exit\nEnter choice: ");
        scanf("%d", &choice);
        getchar();  // to consume newline

        switch (choice) {
            case 1:
                addStudent(students, &count);
                break;
            case 2:
                displayStudents(students, count);
                break;
        }
    } while (choice != 3);

    return 0;
}

void addStudent(struct Student students[], int *count) {
    if (*count >= MAX) {
        printf("Limit reached!\n");
        return;
    }

    printf("Enter roll number: ");
    scanf("%d", &students[*count].roll);
    getchar();
    printf("Enter name: ");
    fgets(students[*count].name, 50, stdin);
    students[*count].name[strcspn(students[*count].name, "\n")] = 0; // remove newline
    printf("Enter marks: ");
    scanf("%f", &students[*count].marks);
    (*count)++;
}

void displayStudents(struct Student students[], int count) {
    printf("Student List:\n");
    for (int i = 0; i < count; i++)
        printf("Roll: %d, Name: %s, Marks: %.2f\n", students[i].roll, students[i].name, students[i].marks);
}
