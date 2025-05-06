#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "input.h"

enum { LETTERS_RANGE = 26 };

char rotate_letter(char, int);

int main(int argc, char* argv[])
{
    if (argc != 2 || !isdigit(*argv[1]))
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    
    char *text = get_string("plaintext:  ");
    int key = (int)strtol(argv[1], (char **)NULL, 10);

    printf("ciphertext: ");

    for (int i = 0; i < strlen(text); i++)
    {
        putchar(rotate_letter(text[i], key));
    }

    putchar('\n');

    return 0;
}

char rotate_letter(char letter, int gap)
{
    if (!islower(letter) && !isupper(letter))
    {
        return letter;
    }

    char aux = (islower(letter)) ? 'a' : 'A';
    int size = (int)letter - aux + gap;
    
    while (size >= LETTERS_RANGE)
    {
        size -= LETTERS_RANGE;
    }


    return size + aux;
}
