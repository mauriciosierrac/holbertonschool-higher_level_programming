#include "lists.h"

/**
 * print_dlistint - print the elements of double list
 * @h: pointer to list
 * Return: numbers of nodes
 */
size_t print_dlistint(const dlistint_t *h)
{
	size_t i = 0;

	while(h != NULL)
	{
		if(h == NULL)
		{
			return (-1);
		}
		else
		{
			printf("%d\n", h->n);
		}
		h = h->next;
		i++;
		
	}	
}