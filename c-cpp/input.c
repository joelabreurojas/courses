#include <stdio.h>
#include <stdlib.h>

#include "input.h"

char *str = NULL;

char *get_string(char *message)
{
    char *aux = NULL;
    int c = 0;
    size_t len = 0;

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

#if defined (__GNUC__)
    static void __attribute__((destructor)) teardown();
#else
    #error Default compiler / version is not recognized.
#endif

void teardown(void)
{
    free(str);
}
