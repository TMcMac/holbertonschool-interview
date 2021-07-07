#include "menger.h"
#include <math.h>
void level_one(void);
/**
 * menger - draws a 2D Menger Sponge
 * @level: level of the Menger Sponge to draw
 *
 * Return: void
 */

void menger(int level)
{
	if (level == 0)
		printf("#\n");

	if (level == 1)
		level_one();
}

/**
 * level_one - print a 2D Menger Sponge
 *
 * Return: void
 */
void level_one(void)
{
	int col, row;

	for (col = 0; col < 3; col++)
	{
		for (row = 0; row < 3; row++)
		{
			if (col == 1 && row == 1)
				printf(" ");
			else
				printf("#");
		}
		printf("\n");
	}
}
