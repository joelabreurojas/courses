#include <stdio.h>

#include "input.h"

const int RANGE = 4;
const int COINS[] = {25, 10, 5, 1};

int calculate_cash(int coin, int money);

int main(void) {
  int money = 0;
  do {
    money = get_int("Money to coins: ");
  } while (money < 0);

  int cash = calculate_cash(25, money);

  printf("Total: %i\n", cash);
}

int calculate_cash(int coin, int money) {
  int cash = 0, total = 0, i = 0;

  for (; i < RANGE && coin != COINS[i]; i++)
    ;

  while (money >= coin) {
    cash++;
    money -= coin;
  }

  if (cash) {
    total += cash;
    printf("%i: %i\n", coin, cash);
  }

  if (money) {
    total += calculate_cash(COINS[i + 1], money);
  }

  return total;
}
