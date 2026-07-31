#include <stdio.h>
#include <ctype.h>
#include <string.h>

int isAlphanumeric(char c) {
    return (isalnum(c));
}

int isPalindrome(char str[]) {
    int start = 0;
    int end = strlen(str) - 1;

    while (start < end) {
        if (!isAlphanumeric(str[start])) {
            start++;
        } else if (!isAlphanumeric(str[end])) {
            end--;
        } else {
            if (tolower(str[start]) != tolower(str[end])) {
                return 0;
            }
            start++;
            end--;
        }
    }
    return 1;
}

int main() {
    char str[1000];

    printf("Enter a string: ");
    fgets(str, sizeof(str), stdin);

    str[strcspn(str, "\n")] = '\0';

    if (isPalindrome(str)) {
        puts("The string is a palindrome");
    } else {
        puts("The string is not a palindrome");
    }

    return 0;
}
