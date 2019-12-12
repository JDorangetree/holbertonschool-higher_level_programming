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
	listint_t *iterator;

	iterator = list;
	while (iterator->next != NULL)
	{
		iterator = iterator->next;
		if (iterator->next == list)
			return (1);
	}
	return (0);
}
