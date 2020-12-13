#include "lists.h"

/**
 * add_dnodeint_end - this function added a new node in the end
 * @head: pointer to pointer head from main
 * @n: value integer
 * Return: node added
 */
dlistint_t *add_dnodeint_end(dlistint_t **head, const int n)
{
	dlistint_t *node, *aux = NULL;

	node = malloc(sizeof(dlistint_t));

	if (node == NULL)
	{
		return (NULL);
	}

	node->n = n;
	node->next = NULL;
	node->prev = NULL;

	if (*head == NULL)
	{
		*head = node;
		return (node);
	}

	for (aux = *head; aux->next != NULL;)
	{
		aux = aux->next;
	}

	aux->next = node;
	node->prev = aux;

	return (node);
}
