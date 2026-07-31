#include <stdio.h>
#include <math.h>

#define SIMPLE
//#define BitMinipulation

#ifdef SIMPLE
int main() {
    char binary[6]; 
    int decimal = 0, length = 0, i;

    printf("Enter a binary number (up to 5 digits): ");
    scanf("%s", binary);

    while (binary[length] != '\0')
        length++;

    for (i = 0; i < length; i++) {
        if (binary[length - 1 - i] == '1')  // if the current digit is 1
            decimal += pow(2, i);           // add 2 raised to the power of the position to the decimal equivalent
    }

    printf("decimal equivalent: %d\n", decimal);

    return 0;
}
#endif

#ifdef BitMinipulation
int main() {
    int binary, decimal = 0, power = 1;

    printf("Enter a binary number (up to 5 digits): ");
    scanf("%d", &binary);

    while (binary > 0) {
        int bit = binary & 1;      // extract the rightmost bit using bitwise AND with 1
        decimal += bit * power;    // add the value of bit to the decimal equivalent
        binary >>= 1;              // shift the binary number to the right to process next bit
        power <<= 1;               // increase power of 2 for the next bit's position
    }

    printf("decimal equivalent: %d\n", decimal);

    return 0;
}
#endif