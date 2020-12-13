#include "lists.h"

/**
 * dlistint_len - print lenght to elements
 * @h: pointer to list
 * Return: numbers of elements
 */
size_t dlistint_len(const dlistint_t *h)
{
	size_t i = 0;

	while (h != NULL)
	{
		if (h == NULL)
		{
			return (-1);
		}
		h = h->next;
		i++;
	}
	return (i);
}
