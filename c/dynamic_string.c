// https://stackoverflow.com/questions/62878982/how-to-make-a-dynamic-string
// by chqrlie

#include <stdio.h>
#include <stdlib.h>

int main() {
    int len = 0;
    char *cad, *new_cad;
    int c;

    printf("word: ");

    cad = malloc(len + 1);
    if (cad == NULL) {
        printf("memory allocation failure\n");
        return 1;
    }
    while ((c = getchar()) != EOF && c != '.') {
        cad[len] = (char)c;
        len++;
        new_cad = realloc(cad, len + 1);
        if (new_cad == NULL) {
            printf("memory allocation failure\n");
            free(cad);
            return 1;
        }
        cad = new_cad;
    }
    cad[len] = '\0';

    printf("tam: %d, string: %s\n", len, cad);
    free(cad);

    return 0;
}

