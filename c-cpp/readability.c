#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

#include "input.h"

int count_letters(char *);
int count_words(char *);
int count_sentences(char *);

int main(int argc, char *argv[])
{
    char *text = get_string("Text: ");
    int words = count_words(text);
    float averrage_letters = (float)count_letters(text) / words * 100;
    float averrage_sentences = (float)count_sentences(text) / words * 100;
    int coleman_index = round(0.0588 * averrage_letters - 0.296 * averrage_sentences - 15.8);

    if (coleman_index <= 1)
        printf("Before Grade 1\n");

    else if (coleman_index > 16)
        printf("Grade 16+\n");

    else
        printf("Grade %i\n", coleman_index);

    return 0;
}

int count_letters(char *text)
{
    int count = 0;

    for (int i = 0, n = strlen(text); i < n; i++)
        count = (isalpha(text[i])) ? count + 1 : count;

    return count;
}

int count_words(char *text)
{
    int count = 1;

    for (int i = 0, n = strlen(text); i < n; i++)
        count = (isspace(text[i])) ? count + 1 : count;

    return count;
}

int count_sentences(char *text)
{
    int count = 0;

    for (int i = 0, n = strlen(text); i < n; i++)
        count = (strchr(".?!", text[i])) ? count + 1 : count;

    return count;
}

