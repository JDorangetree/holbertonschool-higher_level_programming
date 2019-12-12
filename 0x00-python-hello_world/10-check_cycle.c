#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Returns the number of element of the list
 * @list: header of the linked list to count the objects
 *
 * Return: 1 if linked list is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *iterator, *tmp;

	if (!list || !list->next)
		return (0);

	iterator = list;
	while (iterator->next != NULL)
	{
		tmp = iterator;
		if (iterator->next == list || tmp <= iterator->next)
			return (1);
		iterator = iterator->next;
	}
	return (0);
}
