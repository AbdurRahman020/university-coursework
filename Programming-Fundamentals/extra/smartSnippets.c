#include <stdio.h>
#include <math.h>

int main() {

    printf("%d\n", printf("Hello"));
    printf("%d\n", printf("%d", printf("%d", 54)));

    if (printf("Hello World\n")) {}
    
    // single for loop for a string pattern
    char c[] = "hello";
    for (int i = 1; i <= 6; i++)
        printf("%.*s\n", i, c); 

    // calculating factorial
    int f = 1, j = 1, n=7;
    for(; j<=n; f*=j, j++ );
    printf("%d\n", f);

    // reverse a number
    int num = 5432, r = 0;
    for (; num; r = r * 10 + num % 10, num /= 10);
    printf("%d\n", r);

    // length of input string
    int x = 0;
    char str[100] = "";
    scanf("%[^\n]%n", str, &x);
    printf("%d\n", x);
    
    // to count numbe of digits of an integer 
    int digit_counts;
    scanf("%d", &digit_counts);
    digit_counts = digit_counts < 0 ? -digit_counts : digit_counts;
    printf("%d\n", digit_counts ? (int)(log10(digit_counts) + 1) : 1);

    // equating two intgers 
    int a, b;
    scanf("%d%d", &a, &b);
    printf("%d\n", !(a^b)); 

    // sum digits of an integer, unitl getting a single digit
    int single_digit;
    scanf("%d", &single_digit);
    printf("%d\n", single_digit % 9 ? single_digit % 9 : single_digit ? 9:0);

    // number is a power of 2
    int power_of_two;
    scanf("%d", &power_of_two);
    printf("%d\n", power_of_two && !(power_of_two & (power_of_two - 1)));

    // hide a message in code that executes without revealing it
    char *msg = "This is a message";
    while (*msg) putchar(*msg++);

    return 0;
}
