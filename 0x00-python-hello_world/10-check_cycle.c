#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: the list should be checked
 * Return: 1 or 0
 */
int check_cycle(listint_t *list)
{
	listint_t *current;

	if (!list || !list->next)
		return (0);
	current = list;
	while (current != NULL)
	{
		current = current->next;
		if (current == list)
			return (1);
	}
	return (0);
}
