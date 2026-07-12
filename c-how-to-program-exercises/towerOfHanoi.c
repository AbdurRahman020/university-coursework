#include <stdio.h>
#include <math.h>

#define ToH
// #define ToHI

// 5.36 Towers of Hanoi
#ifdef ToH
void moveDisks(int n, int src, int dest, int aux) {
    // base case: when there is only one disk to move
    if (n == 1) {
        printf("%d → %d\n", src, dest);
        return;
    }

    // step 1: move n-1 disks from source to auxiliary, using destination as auxiliary
    moveDisks(n - 1, src, aux, dest);

    // step 2: move the nth disk from source to destination
    printf("%d → %d\n", src, dest);

    // step 3: move the n-1 disks from auxiliary to destination, using source as auxiliary
    moveDisks(n - 1, aux, dest, src);
}

int main() {
    int num_of_disks;

    printf("Enter the number of disks: ");
    scanf("%d", &num_of_disks);

    moveDisks(num_of_disks, 1, 3, 2);
	
    return 0;
}
#endif

// 5.37 Towers of Hanoi (Iterative)
#ifdef ToHI
void moveDisksIteratively(int n, int src, int dest, int aux) {
    // calculate the total number of moves (2^n - 1)
    int totalMoves = (1 << n) - 1;
    int move, from, to;

    // if n is even, swap destination and auxiliary pegs
    if (n % 2 == 0) {
        int temp = dest;
        dest = aux;
        aux = temp;
    }

    // perform the moves
    for (move = 1; move <= totalMoves; move++) {
        // determine the move: depending on the move number, choose the correct peg
        if (move % 3 == 1) {
            from = src;
            to = dest;
        } else if (move % 3 == 2) {
            from = src;
            to = aux;
        } else {
            from = aux;
            to = dest;
        }

        printf("%d → %d\n", from, to);
    }
}

int main() {
    int num_of_disks;

    printf("Enter the number of disks: ");
    scanf("%d", &num_of_disks);

    moveDisksIteratively(num_of_disks, 1, 3, 2);

    return 0;
}
#endif