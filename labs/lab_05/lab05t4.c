#include <stdio.h>

int calculate_Easter_date(int);

int main() {
    FILE *input = fopen("years.txt", "r");
    FILE *output = fopen("easter_dates.txt", "w");
    int year, result;
    
    if (input == NULL || output == NULL) {
        perror("Error opening file");
        return 1;
    }
    
    while (fscanf(input, "%d", &year) != EOF) {
        result = calculate_Easter_date(year);
        if (result > 0)
            fprintf(output, "%d - April %d\n", year, result);
        else
            fprintf(output, "%d - March %d\n", year, -result);
    }
    
    fclose(input);
    fclose(output);
    
    return 0;
}

int calculate_Easter_date(int Y) {
    int G, C, X, Z, D, E, N;
    
    G = Y % 19 + 1;
    C = Y / 100 + 1;
    X = 3 * C / 4 - 12;
    Z = (8 * C + 5) / 25 - 5;
    D = 5 * Y / 4 - X - 10;
    
    E = (11 * G + 20 + Z - X) % 30;
    
    if (E == 25 && G > 11) {
        E++;
    }
    
    if (E == 24) {
        E++;
    }
    
    N = 44 - E;
    
    if (N < 21) {
        N += 30;
    }
    
    N = N + (D + N) % 7;
    
    if (N > 31)
        return N - 31;
    else
        return -N;
}
