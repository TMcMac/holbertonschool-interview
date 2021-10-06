#include "lists.h"
/**
 * find_listint_loop - a function to search for a loop in
 * singly linked list
 * @head: a pointer to the head of a list
 * Return: The address to the node where a loop starts or
 * NULL if there is no loop.
 */


listint_t *find_listint_loop(listint_t *head)
{
	listint_t *tort;
	listint_t *hare;

	tort = hare = head;

	if (head == NULL || head->next == NULL)
		return (NULL);

	while (hare->next && hare->next->next)
	{
		tort = tort->next;
		hare = hare->next->next;
		if (tort == hare)
		{
			tort = head;
			while (tort->next != head)
				tort = tort->next;
			return (tort);
		}
	}
	return (NULL);
}
