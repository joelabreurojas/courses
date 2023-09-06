#include <float.h>
#include <limits.h>
#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

#include "input.h"

char *str = NULL;


char get_char(char *message)
{
    while(true)
    {
        char *input = get_string(message);
        if (!input)
        {
            return CHAR_MAX;
        }

        char c, i;
        if (sscanf(input, "%c%c", &c, &i) == 1)
        {
            return c;
        }
    }
}

double get_double(char *message)
{
    while(true)
    {
        char *input = get_string(message);
        if (!input)
        {
            return DBL_MAX;
        }

        char c;
        double d = 0;

        if (sscanf(input, "%lg%c", &d, &c) == 1)
        {
            return d;
        }
    }
}

float get_float(char *message)
{
    while(true)
    {
        char *input = get_string(message);
        if (!input)
        {
            return FLT_MAX;
        }

        char c;
        float f = 0;

        if (sscanf(input, "%g%c", &f, &c) == 1)
        {
            return f;
        }
    }
}

int get_int(char *message)
{
    while(true)
    {
        char *input = get_string(message);
        if (!input)
        {
            return INT_MAX;
        }

        char c;
        int i = 0;

        if (sscanf(input, "%i%c", &i, &c) == 1)
        {
            return i;
        }
    }
}

long get_long(char *message)
{
    while(true)
    {
        char *input = get_string(message);
        if (!input)
        {
            return LONG_MAX;
        }

        char c;
        long l = 0;

        if (sscanf(input, "%li%c", &l, &c) == 1)
        {
            return l;
        }
    }
}

char *get_string(char *message)
{
    char *aux = NULL;
    int c = 0;
    size_t len = 0;

    printf("%s", message);

    str = malloc(1);
    if (!str)
    {
        return NULL;
    }

    while ((c = fgetc(stdin)) != '\n' && c != EOF)
    {
        if (len + 1 > SIZE_MAX)
        {
            return NULL;
        }

        str[len] = (char)c;
        len++;

        aux = realloc(str, len);
        if (!aux)
        {
            return NULL;
        }
        str = aux;
    }

    str[len] = '\0';

    return str;
}

#if defined (__GNUC__)
    void __attribute__((destructor)) cleanup();
#else
    #error Default compiler / version is not recognized.
#endif

void cleanup(void)
{
    free(str);
}
