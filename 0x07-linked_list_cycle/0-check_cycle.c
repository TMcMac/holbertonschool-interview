#include "lists.h"

/**
 *
 *
 *
 *
 */

int check_cycle(listint_t *list)
{
  listint_t *hare = list, *tort = list;

  if (list == NULL || list->next == NULL)
    return(0);

  while (hare != NULL && tort != NULL)
    {
      if (hare->next->next != NULL)
	{
	  hare = hare->next->next;
	  tort = tort->next;
	}
      else
	return(0);
      if (tort == hare)
	return(1);
      
    }
  return(0);
}
