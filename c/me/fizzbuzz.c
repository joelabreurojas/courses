#include <stdio.h>

#include "input.h"

int main(int argc, char *argv[])
{
    char c = 0;
    int input = get_int("Integer input: ");

    for (int i = 1; i <= input; i++)
    {
        if (i % 3 == 0)
        {
            printf("Fizz");
        }

        if (i % 5 == 0)
        {
            printf("Buzz");
        }

        if ((i % 3 != 0) && (i % 5 != 0))
        {
            printf("%i", i);
        }

        putchar('\n');
    }

    return 0;
}
