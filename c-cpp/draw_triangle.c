#include <stdbool.h>
#include <stdio.h>

int get_size(void);
void print_spaces(int, int);
void print_blocks(int, bool);

int main(void)
{
    int size = get_size();
    for(int rows = 0; rows < size; rows++)
    {
        print_spaces(rows, size);
        printf("#");
        print_blocks(rows, true);
    }

    return 0;
}

int get_size(void)
{
    int size = 0;
    do 
    {
        printf("Size (3-9): ");
        scanf("%i", &size);
    }
    while(size < 1 || size > 9);
    return size;
}

void print_spaces(int rows, int size)
{
    for (int spaces = size - rows; spaces > 0; spaces--)
    {
        printf(" ");
    }
    print_blocks(rows, false);
}

void print_blocks(int rows, bool jump)
{
    for (int blocks = 0; blocks < rows; blocks++)
    {
        printf("#");
    }

    if (jump == true) printf("\n");
}
