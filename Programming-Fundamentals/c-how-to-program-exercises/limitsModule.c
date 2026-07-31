#include <stdio.h>
#include <limits.h>

int main() {
    printf("Maximum value for int: %d\n", INT_MAX);
    printf("Minimum value for int: %d\n", INT_MIN);
    printf("Maximum value for unsigned int: %u\n", UINT_MAX);
    printf("Maximum value for long: %ld\n", LONG_MAX);
    printf("Maximum value for unsigned long: %lu\n", ULONG_MAX);
    printf("Maximum value for long long: %lld\n", LLONG_MAX);
    printf("Maximum value for unsigned long long: %llu\n", ULLONG_MAX);
    
    return 0;
}
