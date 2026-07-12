#include <stdio.h>

#define MAZE_SIZE 12

int dRow[] = {0, 1, 0, -1};
int dCol[] = {1, 0, -1, 0};

void printMaze(char maze[MAZE_SIZE][MAZE_SIZE]) {
    for (int i = 0; i < MAZE_SIZE; i++) {
        for (int j = 0; j < MAZE_SIZE; j++) 
            printf("%c ", maze[i][j]);
        puts("");
    }
    puts("");
}

int mazeTraverse(char maze[MAZE_SIZE][MAZE_SIZE], int row, int col, int direction) {
    if (row < 0 || row >= MAZE_SIZE || col < 0 || col >= MAZE_SIZE || maze[row][col] == '#' || maze[row][col] == 'X') 
        return 0;

    maze[row][col] = 'X';

    printMaze(maze);

    if ((row == 0 || row == MAZE_SIZE - 1 || col == 0 || col == MAZE_SIZE - 1) && maze[row][col] == 'X')
        return 1;

    for (int i = 0; i < 4; i++) {
        int newDirection = (direction + i) % 4;
        int newRow = row + dRow[newDirection];
        int newCol = col + dCol[newDirection];

        if (mazeTraverse(maze, newRow, newCol, newDirection))
            return 1; 
    }

    maze[row][col] = '.';
    return 0; 
}

int main() {
    char maze[MAZE_SIZE][MAZE_SIZE] = {
        {'#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'},
        {'#', '.', '.', '.', '#', '.', '.', '.', '.', '.', '.', '#'},
        {'.', '.', '#', '.', '#', '.', '#', '#', '#', '#', '.', '#'},
        {'#', '#', '#', '.', '#', '.', '.', '.', '.', '#', '.', '#'},
        {'#', '.', '.', '.', '.', '#', '#', '#', '.', '#', '.', '.'},
        {'#', '#', '#', '#', '.', '#', '.', '#', '.', '#', '.', '#'},
        {'#', '.', '.', '#', '.', '#', '.', '#', '.', '#', '.', '#'},
        {'#', '#', '.', '#', '.', '#', '.', '#', '.', '#', '.', '#'},
        {'#', '.', '.', '.', '.', '.', '.', '.', '#', '.', '#', '#'},
        {'#', '#', '#', '#', '#', '#', '.', '#', '#', '#', '.', '#'},
        {'#', '.', '.', '.', '.', '.', '#', '.', '.', '.', '#', '#'},
        {'#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'}
    };

    int startRow = 1, startCol = 1;
    
    if (!mazeTraverse(maze, startRow, startCol, 0))
        printf("No solution found.\n");
    else
        printf("Exit found!\n");

    return 0;
}
