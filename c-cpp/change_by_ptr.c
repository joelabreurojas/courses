#include <stdio.h>
#include <stdlib.h>

void changeStage(char *str){
    str[0] = '0'; // by index
    str++;  // by increment
    *str = '1';
}

int main(void)
{
    char *str = NULL;

    str = malloc(2);

    // After
    printf("str: %s\n", str);

    changeStage(str);

    // Before
    printf("str: %s\n", str);
    return 0;
}
