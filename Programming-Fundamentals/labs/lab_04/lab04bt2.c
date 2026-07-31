#include <stdio.h>
#include <string.h>

int main() {
    char username[] = "a";
    char password[] = "123";
    char input_username[20], input_password[20];

    while (1) {
        printf("Enter Username and Password: ");
        scanf("%19s, %19s", input_username, input_password);

        if (strcmp(input_username, username) == 0 && strcmp(input_password, password) == 0) {
            puts("Login Successful.");
            break;
        } else {
            puts("Incorrect Username or Password. Try again.");
        }
    }

    return 0;
}
