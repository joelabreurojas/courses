#include "input.h"

int calculate_quarters(int cents);

int main(void)
{
    int cents = 0;
    do
    {
        cents = get_int("Change owed:");
    }
    while (cents < 0);

    int quarters = calculate_quarters(cents);

    cents = cents - (quarters * 25);
}

int calculate_quarters(int cents)
{
    int quarters = 0;

    while (cents >= 25)
    {
        quarters++;
        cents = cents - 25;
    }

    return quarters;
}
