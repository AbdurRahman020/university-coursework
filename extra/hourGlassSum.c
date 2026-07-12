#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

#define R 5
#define C 5

int maxSum(int arr[R][C]) {
	int i, j, sum;
    
	if (R<3 || C<3) {
		printf("not possible!");
		exit(0);
	}

	int max_sum = INT_MIN;
    
	for (i = 0; i < R - 2; i++) {
		for (j = 0; j < C - 2; j++) {
			sum = (arr[i][j] + arr[i][j + 1] + arr[i][j + 2]) + (arr[i + 1][j + 1])
				+ (arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2]);

			if (sum > max_sum)
				max_sum = sum;
			else
				continue;
		}
	}

	return max_sum;
}

int main() {
	int arr[][C] = {{1, 2, 3, 0, 0},
			{0, 0, 0, 0, 0},
			{2, 1, 4, 0, 0},
			{0, 0, 0, 0, 0},
			{1, 1, 0, 1, 0}};

	int res = maxSum(arr);
	printf("maximum hour glass sum is: %d", res);
	
	return 0;
}
