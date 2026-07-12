#include <stdio.h>

void decimalToRoman(int num) {
    char *romanNumerals[] = {"I", "IV", "V", "IX", "X", "XL", "L", "XC", "C"};
    int values[] = {1, 4, 5, 9, 10, 40, 50, 90, 100};
    
    int i = 8;
    
    while (num > 0) {
        while (num >= values[i]) {
            printf("%s", romanNumerals[i]);
            num -= values[i];
        }
        i--;
    }
}

int main() {
    puts("Decimal to Roman Numeral Conversion Table (1 to 100):");
    puts("-----------------------------------------------------");
    puts("Decimal | Roman");
    puts("--------|--------------");

    for (int i = 1; i <= 100; i++) {
        printf("%7d  | ", i);
        decimalToRoman(i);
        printf("\n");
    }

    return 0;
}
