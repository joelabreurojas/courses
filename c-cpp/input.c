#include <float.h>
#include <limits.h>
#include <stdarg.h>
#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

#include "input.h"

char *str = NULL;

char get_char(const char *message)
{
    char c, i, *input = NULL;

    do
    {
        input = get_string(message);
        if (!input)
        {
            return CHAR_MAX;
        }
    }
    while (!sscanf(input, "%c%c", &c, &i));

    return c;
}

double get_double(const char *message)
{
    char c, *input = NULL;
    double d = 0;

    do
    {
        input = get_string(message);
        if (!input)
        {
            return DBL_MAX;
        }
    }
    while (!sscanf(input, "%lg%c", &d, &c));

    return d;
}

float get_float(const char *message)
{
    char c, *input = NULL;;
    float f = 0;

    do
    {
        input = get_string(message);
        if (!input)
        {
            return FLT_MAX;
        }
    }
    while (!sscanf(input, "%g%c", &f, &c));

    return f;
}

int get_int(const char *message)
{
    char c, *input = NULL;
    int i = 0;

    do
    {
        input = get_string(message);
        if (!input)
        {
            return INT_MAX;
        }
    }
    while (!sscanf(input, "%i%c", &i, &c));

    return i;
}

long get_long(const char *message)
{
    char c, *input = NULL;
    long l = 0;

    do
    {
        input = get_string(message);
        if (!input)
        {
            return LONG_MAX;
        }

    }
    while (!sscanf(input, "%li%c", &l, &c));

    return l;
}

char *get_string(const char *message)
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
