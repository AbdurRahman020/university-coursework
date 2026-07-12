#include <stdio.h>

int main() {
    double current_population = 8000000000.0;
    double growth_rate = 0.011;
    int years = 100;

    double double_population = current_population * 2;
    double quadruple_population = current_population * 4;
    int population_doubled_year = -1;
    int population_quadrupled_year = -1;

    printf("%-6s %-20s %-20s\n", "Year", "Population", "Annual Increase");

    for (int year = 1; year <= years; year++) {
        double population_increase = current_population * growth_rate;

        current_population += population_increase;

        if (population_doubled_year == -1 && current_population >= double_population) {
            population_doubled_year = year;
            printf("Year %d: Population has doubled.\n", year);
        }
        
        if (population_quadrupled_year == -1 && current_population >= quadruple_population) {
            population_quadrupled_year = year;
            printf("Year %d: Population has quadrupled.\n", year);
        }

        printf("%-6d %-20.0f %-20.0f\n", year, current_population, population_increase);
    }

    if (population_doubled_year == -1) {
        printf("Population has not yet doubled after %d years.\n", years);
    }
    
    if (population_quadrupled_year == -1) {
        printf("Population has not yet quadrupled after %d years.\n", years);
    }

    return 0;
}
