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

    if (!(luhn_algorithm(card_numbers)))
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
            count = i;
        }
    }
    while (strlen(input) != count && count != LENGTH);

    return input;
}

bool luhn_algorithm(char *card)
{
    int addition = 0; 

    for (int i = 0, product = 0; i < LENGTH; i += 2)
    {
        if ((product = (card[i] - '0') * 2) > 9)
        {
            product -= 9;
        }

        addition += product + card[i + 1] - '0';
    }

    return (!(addition % 10));
}
