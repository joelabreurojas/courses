#include <stdio.h>
#include <stdlib.h>

static char *aux = NULL;
static char *str = NULL;
static size_t len = 0;

static char *get_string(char *message)
{
    int c = 0;

    printf("%s", message);

    str = malloc(len + 1);
    while ((c = getchar()) != '\n' && c != EOF)
    {
        str[len] = (char)c;
        len++;
        aux = realloc(str, len + 1);
        str = aux;
    }
    str[len] = '\0';

    return str;
}
