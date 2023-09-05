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

    str = malloc(1);
    while ((c = fgetc()) != '\n' && c != EOF)
    {
        str[len] = (char)c;
        len++;
        aux = realloc(str, len);
        str = aux;
    }
    str[len] = '\0';

    return str;
}

#if defined (__GNUC__)
    static void __attribute__((destructor)) cleanup();
#else
    #error Default compiler / version is not recognized.
#endif

void cleanup(void)
{
    free(str);
}
