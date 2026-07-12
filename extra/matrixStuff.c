#include <stdio.h>

// #define MatrixMultplication
#define SparseMatrix

#ifdef MatrixMultplication
int main() {
    int n, m, c, d, p, q, k, first[10][10], second[10][10], pro[10][10], sum = 0;

    printf("Enter the number of rows and columns of the first matrix:\n");
    scanf("%d%d", &m, &n);
    
    printf("Enter the %d elements of the first matrix:\n", m*n);
    for(c = 0; c < m; c++) {    // to iterate the rows
		for(d = 0; d < n; d++) {    // to iterate the columns
			scanf("%d", &first[c][d]);
		}
	}
	
    printf("Enter the number of rows and columns of the second matrix:\n");
    scanf("%d%d", &p, &q);

    if(n != p)
        printf("Matrices with the given order cannot be multiplied with each other.\n");
    else {   // matrices can be multiplied
        printf("Enter the %d elements of the second matrix:\n",m*n);

        for(c = 0; c < p; c++) {    // to iterate the rows
			for(d = 0; d < q; d++) {   // to iterate the columns
				scanf("%d", &second[c][d]);
			}
		}
        // printing the first matrix
        printf("The first matrix is:\n");
        for(c = 0; c < m; c++) {    // to iterate the rows
            for(d = 0; d < n; d++) {    // to iterate the columns
                printf("%d\t", first[c][d]);
            }
            puts("");
        }

        // printing the second matrix
        printf("The second matrix is:\n");
        for(c = 0; c < p; c++) {    // to iterate the rows
            for(d = 0; d < q; d++) {    // to iterate the columns
                printf("%d\t", second[c][d]);
            }
            puts("");
        }

        for(c = 0; c < m; c++) {    // to iterate the rows
            for(d = 0; d < q; d++) {    // to iterate the columns
                for(k = 0; k < p; k++) {
                    sum += first[c][k]*second[k][d];
				}
            pro[c][d] = sum;	// resultant element of pro after multiplication
            sum = 0;	// to find the next element from scratch
            }
        }

        // printing the elements of the product matrix
        printf("The multiplication of the two entered matrices is:\n");
        for(c = 0; c < m; c++) {    // to iterate the rows
            for(d = 0; d < q; d++) {    // to iterate the columns
                printf("%d\t", pro[c][d]);
            }
            puts("\n");   // to take the control to the next row
        }
    }

    return 0;
}
#endif

#ifdef SparseMatrix
int main()
{
    int n, m, c, d, matrix[10][10];
    int counter = 0;

    printf("Enter the number of rows and columns of the matrix:\n");
    scanf("%d%d", &m, &n);

    printf("\nEnter the %d elements of the matrix:\n",m*n);
    for(c = 0; c < m; c++) {    // to iterate the rows
        for(d = 0; d < n; d++) {    // to iterate the columns
            scanf("%d", &matrix[c][d]);
            if(matrix[c][d] == 0)
            counter++;
        }
    }

    // printing the matrix
    printf("\nThe entered matrix is:\n");
    for(c = 0; c < m; c++) {    // to iterate the rows
        for(d = 0; d < n; d++) {    // to iterate the columns
            printf("%d\t", matrix[c][d]);
        }
        puts("\n"); // to take the control to the next row
    }

    // checking if the matrix is sparse or not
    if(counter > (m*n)/2)
        printf("The entered matrix is a sparse matrix.\n");
    else
        printf("The entered matrix is not a sparse matrix.\n");
    
    return 0;
}
#endif
