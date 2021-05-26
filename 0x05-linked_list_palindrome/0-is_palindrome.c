#include "lists.h"

/**
 * is_palindrome - a function to check if a singly linked
 * list is or is not a palindrome (same forwars and backwards)
 * @head: a double pointer to the head (node 0) of the list
 * Return: 1 ifthe list is a Plindrome or 0 if it isnt
 */

int is_palindrome(listint_t **head)
{
	int count = 0;
	int i = 0;
	listint_t *mover;
	int *listn;

	if (!head)
		return (0);
	if (!*head)
		return (1);

	mover = *head;
	if (mover->next == NULL)
		return (1);

	while (mover != NULL)
	{
		count++;
		mover = mover->next;
	}
	listn = malloc(sizeof(int) * count);
	if (listn == NULL)
		return (0);
	mover = *head;
	while (mover != NULL)
	{
		listn[i] = mover->n;
		i++;
		mover = mover->next;
	}
	mover = *head;
	while (mover != NULL)
	{
		if (listn[i - 1] == mover->n)
		{
			i--;
			mover = mover->next;
		}
		else
			return (0);
	}
	return (1);
}
