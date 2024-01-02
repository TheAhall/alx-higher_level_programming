#include "lists.h"
#include <stdlib.h>
#include <unistd.h>

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: that list
 * @number: the number
 * Rturn: the new list
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp1, *tmp2, *new;

	if (head == NULL)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	tmp1 = *head;
	if (!*head || (*head)->n > number)
	{
		new->next = *head;
		*head = new;
		return (*head);
	}
	else
	{
		while (tmp1 != NULL && tmp1->n < number)
		{
			tmp2 = tmp1;
			tmp1 = tmp1->next;
		}
		tmp2->next = new;
		new->next = tmp1;
	}
	return (new);
}
