#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: the list should be checked
 * Return: 1 or 0
 */
int check_cycle(listint_t *list)
{
	listint_t *lst1, *lst2;

	if (!list || !list->next)
		return (0);
	lst1 = list;
	lst2 = list;
	while (lst1 != NULL && lst2 != NULL && lst2->next != NULL)
	{
		lst1 = lst1->next;
		lst2 = lst2->next->next;
		if (lst1 == lst2)
			return (1);
	}
	return (0);
}
