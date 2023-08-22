#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>

#define LENGTH 16

int *arrchar_to_arrint(char *);
char *get_input(void);
bool luhn_algorithm(int *);

int main(void)
{
    char *input = get_input();
    int *card_numbers = arrchar_to_arrint(input);

    if (luhn_algorithm(card_numbers))
    {
        printf("VALID\n");
        return 0;
    }

    printf("INVALID\n");
    return 1;
}

char *get_input(void)
{
    static char input[LENGTH];
    int input_len = 0;

    do
    {
        printf("Number (16 digits): ");
        scanf("%s", input);
        printf("%s", input);
        printf("%li", strlen(input));
    }
    while (strlen(input) != LENGTH);

    return input;
}

int *arrchar_to_arrint(char *arr)
{
    static int numbers[LENGTH];

    for (int i = 0; i < LENGTH; i++)
    {
        if (isdigit(arr[i]))
            numbers[i] = arr[i] - '0';
    }

    return numbers;
}

bool luhn_algorithm(int *arr)
{
    int aux = 0; 

    for (int i = 0; i < LENGTH; i += 2)
        aux += (arr[i] * 2) + arr[i + 1];

    return (aux % 10 == 0);
}
