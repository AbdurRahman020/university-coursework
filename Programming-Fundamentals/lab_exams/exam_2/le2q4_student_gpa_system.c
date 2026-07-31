#include <stdio.h>

#define MAX_STUDENTS 150
#define MAX_COURSES 10

typedef struct {
    char courseName[50];
    int creditHours;
    float grade; // 0.0 to 4.0 scale
} Course;

typedef struct {
    char name[50];
    int age;
    char department[30];
    char mobile[15];
    int courseCount;
    Course courses[MAX_COURSES];
} Student;

// function prototypes
void addStudent(Student students[], int *count);
void displayStudents(Student students[], int count);
float calculateGPA(Course courses[], int courseCount);

int main() {
    Student students[MAX_STUDENTS];
    int studentCount = 0;
    int choice;

    do {
        printf("\nStudent Record Menu:\n");
        printf("1. Add Student\n");
        printf("2. Display Students\n");
        printf("3. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                addStudent(students, &studentCount);
                break;
            case 2:
                displayStudents(students, studentCount);
                break;
            case 3:
                printf("Exiting program.\n");
                break;
            default:
                printf("Invalid choice. Try again.\n");
        }
    } while (choice != 3);

    return 0;
}

void addStudent(Student students[], int *count) {
    // Check if array is full
    if (*count >= MAX_STUDENTS) {
        printf("Maximum student limit reached.\n");
        return;
    }

    Student *s = &students[*count]; // pointer to new student slot

    // get student details
    printf("Enter name: ");
    scanf(" %[^\n]", s->name); // read string with spaces
    printf("Enter age: ");
    scanf("%d", &s->age);
    printf("Enter department: ");
    scanf(" %[^\n]", s->department);
    printf("Enter mobile number: ");
    scanf(" %[^\n]", s->mobile);

    printf("Enter number of courses: ");
    scanf("%d", &s->courseCount);

    // get course details
    for (int i = 0; i < s->courseCount; i++) {
        printf("\nCourse #%d\n", i + 1);
        printf("Enter course name: ");
        scanf(" %[^\n]", s->courses[i].courseName);
        printf("Enter credit hours: ");
        scanf("%d", &s->courses[i].creditHours);
        printf("Enter grade (0.0 - 4.0): ");
        scanf("%f", &s->courses[i].grade);
    }

    (*count)++; // increment student count
    printf("\nStudent added successfully!\n");
}

void displayStudents(Student students[], int count) {
    if (count == 0) {
        printf("\nNo students to display.\n");
        return;
    }

    for (int i = 0; i < count; i++) {
        Student s = students[i];
        
        printf("\n--- Student #%d ---\n", i + 1);
        printf("Name: %s\n", s.name);
        printf("Age: %d\n", s.age);
        printf("Department: %s\n", s.department);
        printf("Mobile: %s\n", s.mobile);
        printf("Courses:\n");

        // display each course
        for (int j = 0; j < s.courseCount; j++) {
            Course c = s.courses[j];
            printf("  %s | Credits: %d | Grade: %.2f\n", 
                   c.courseName, c.creditHours, c.grade);
        }

        // calculate and display GPA
        float gpa = calculateGPA(s.courses, s.courseCount);
        printf("GPA: %.2f\n", gpa);
    }
}

float calculateGPA(Course courses[], int courseCount) {
    float totalPoints = 0;
    int totalCredits = 0;

    // sum weighted grades
    for (int i = 0; i < courseCount; i++) {
        totalPoints += courses[i].grade * courses[i].creditHours;
        totalCredits += courses[i].creditHours;
    }

    return (totalCredits == 0) ? 0.0 : totalPoints / totalCredits;
}
