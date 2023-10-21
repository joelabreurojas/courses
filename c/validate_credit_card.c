#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>

#include "input.h"

#define LENGTH 16

char *get_input(void);
bool luhn_algorithm(char *);

int main(void)
{
    char *card_numbers = get_input();

    if (luhn_algorithm(card_numbers) != 0)
    {
        printf("INVALID\n");
        return 1;
    }

    printf("VALID\n");
    return 0;
}

char *get_input(void)
{
    char *input = NULL;
    int count = 0;

    do
    {
        input = get_string("Number (16 digits): ");

        for (int i = 0; i < LENGTH && isdigit(input[i]); i++)
        {
            count++;
        }
    }
    while (strlen(input) != count && count != LENGTH);

    return input;
}

bool luhn_algorithm(char *card)
{
    int result = 0; 

    for (int i = 0, aux; i < LENGTH; i += 2)
    {
        if ((aux = (card[i] - '0') * 2) > 9)
        {
            aux -= 9;
        }

        result += aux + card[i + 1] - '0';
    }

    return (result % 10);
}
