#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

#include "input.h"

const int RANGE = 26;
const int OFFSET = 'A';

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./substitution KEY\n");

        return 1;
    }

    if (strlen(argv[1]) != RANGE)
    {
        printf("Key must contain %i characters.\n", RANGE);

        return 1;
    }

    int count[RANGE];

    for (int i = 0; i < RANGE; i++)
    {
        count[i] = 0;
    }

    for (int i = 0; i < RANGE; i++)
    {
        if (isdigit(argv[1][i]))
        {
            printf("Key must only contain alphabetic characters.\n");

            return 1;
        }

        count[toupper(argv[1][i]) - OFFSET]++;
    }

    for (int i = 0; i < RANGE; i++)
    {
        if (count[i] > 1)
        {
            printf("Key shouldn't contain duplicate characters.\n");

            return 1;
        }
    }

    char *input = get_string("plaintext: ");
    
    for (int i = 0; i < RANGE; i++)
    {
        if (isalpha(input[i]))
        {
            char cipher = argv[1][toupper(input[i]) - OFFSET];

            input[i] = (isupper(input[i])) ? toupper(cipher) : tolower(cipher);
        }
    }

    printf("cyphertext: %s\n", input);

    return 0;
}
