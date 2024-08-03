#include <ctype.h>
#include <stdio.h>
#include <string.h>

//                         A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z
const int SCORE_BOARD[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 9, 1, 1, 1, 1, 4, 4, 8, 4, 9};

int get_score(char []);

int main(void)
{
    char words[2][30];
    int scores[] = {0, 0};

    printf("Player 1: ");
    scanf("%s", words[0]);
    printf("Player 2: ");
    scanf("%s", words[1]);

    scores[0] = get_score(words[0]);
    scores[1] = get_score(words[1]);

    if (scores[0] > scores[1])
    {
        printf("Player 1 wins!");
    }
    else if (scores[0] < scores[1])
    {
        printf("Player 2 wins!");
    }
    else
    {
        printf("Tie!");
    }
    
    return 0;
}

int get_score(char word[])
{
    int score = 0;

    for (int i = 0; i < strlen(word); i++)
    {
        score += SCORE_BOARD[toupper(word[i]) - 'A'];
    }

    return score;
}
