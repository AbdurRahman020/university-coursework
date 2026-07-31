#include <stdio.h>

int main() {
    float lahore_temp, murree_temp;

    printf("Enter the temperature of Lahore (in Celsius): ");
    scanf("%f", &lahore_temp);
    
    printf("Enter the temperature of Murree (in Celsius): ");
    scanf("%f", &murree_temp);

    if (lahore_temp >= 40) {
        if (murree_temp <= 20)
            printf("Let’s visit Murree.\n");
        else
            printf("Murree tour is not essential.\n");
    }
    else
        printf("Murree tour is not essential.\n");

    return 0;
}
