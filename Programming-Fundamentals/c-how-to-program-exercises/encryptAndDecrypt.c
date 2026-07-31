#include <stdio.h>

// #define ENCRYPT
#define DECRYPT  

#ifdef ENCRYPT
// 3.47 Enforcing Privacy with Cryptography (a)
void encrypt(int);

int main() {
    int number;

    printf("enter a four-digit integer to encrypt: ");
    scanf("%d", &number);

    encrypt(number);

    return 0;
}

void encrypt(int number) {
    int d1 = (number / 1000) % 10;
    int d2 = (number / 100) % 10;
    int d3 = (number / 10) % 10;
    int d4 = number % 10;

    d1 = (d1 + 7) % 10;
    d2 = (d2 + 7) % 10;
    d3 = (d3 + 7) % 10;
    d4 = (d4 + 7) % 10;

    int temp = d1;
    d1 = d3;
    d3 = temp;

    temp = d2;
    d2 = d4;
    d4 = temp;

    printf("encrypted number: %d%d%d%d\n", d1, d2, d3, d4);
}
#endif

#ifdef DECRYPT
// 3.47 Enforcing Privacy with Cryptography (b)
void decrypt(int);

int main() {
    int encrypted_number;

    printf("enter the encrypted four-digit integer to decrypt: ");
    scanf("%d", &encrypted_number);

    decrypt(encrypted_number);

    return 0;
}

void decrypt(int encrypted_number) {
    int d1 = (encrypted_number / 1000) % 10;
    int d2 = (encrypted_number / 100) % 10;
    int d3 = (encrypted_number / 10) % 10;
    int d4 = encrypted_number % 10;

    int temp = d1;
    d1 = d3;
    d3 = temp;

    temp = d2;
    d2 = d4;
    d4 = temp;

    d1 = (d1 - 7 + 10) % 10;
    d2 = (d2 - 7 + 10) % 10;
    d3 = (d3 - 7 + 10) % 10;
    d4 = (d4 - 7 + 10) % 10;

    printf("decrypted number: %d%d%d%d\n", d1, d2, d3, d4);
}
#endif 