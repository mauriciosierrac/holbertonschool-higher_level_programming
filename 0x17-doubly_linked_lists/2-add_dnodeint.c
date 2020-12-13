#include "lists.h"

/**
 * add_dnodeint - add one node to beginning
 * @head: doble pointer to pointer head of main
 * @n: integer value of 'n' element to list
 * Return: the node added
 */
dlistint_t *add_dnodeint(dlistint_t **head, const int n)
{
	dlistint_t *node;

	node = malloc(sizeof(dlistint_t));

	if (node == NULL)
	{
		return (NULL);
	}

	node->next = NULL;
	node->prev = NULL;
	node->n = n;

	/* if the list is empty*/
	if (*head == NULL)
	{
		*head = node;
		return (node);
	}

	node->next = *head;
	(*head)->prev = node;
	*head = node;

	return (node);
}
