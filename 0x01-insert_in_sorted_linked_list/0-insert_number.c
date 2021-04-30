#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - creats a new node with supplied number and
 * inserts the new node into the list at the proper place
 * @head: pointer to the head of a listint_t list
 * @number: the number to be added to new node, and position
 * determining factor
 * Return: address of the new node of NULL if error/failure
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;

	if (head == NULL)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL)
	{
		*head = new;
		return (new);
	}

	current = *head;
	if (new->n < current->n)
	{
		*head = new;
		new->next = current;
		return (new);
	}

	while (current->next != NULL && number > current->next->n)
		current = current->next;

	new->next = current->next;
	current->next = new;

	return (new);
}