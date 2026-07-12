#include <stdio.h>
#include <time.h>

typedef long long ll;

int main() {
    ll count = 1;
    ll limit = 1000000000; // stop when we reach 1,000,000,000
    ll milestone = 100000000; // the milestone to print every 100 million

    clock_t start_time, end_time;
    double elapsed_time;

    start_time = clock();

    while (count <= limit) {
        if (count % milestone == 0)
            printf("Reached: %lld\n", count);
        
        count++;
    }

    end_time = clock();

    elapsed_time = (double)(end_time - start_time) / CLOCKS_PER_SEC;

    printf("\nTime taken to count to %lld: %.2f seconds\n", limit, elapsed_time);

    return 0;
}
