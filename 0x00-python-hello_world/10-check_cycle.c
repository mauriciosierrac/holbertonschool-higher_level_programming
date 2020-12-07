#include "lists.h"

/**
 * check_cycle - Linked list
 * @list: pointer to list
 * Return: 0 if positive circle, 1 negative to circle
 */

int check_cycle(listint_t *list)
{
listint_t *slow = list;
listint_t *fast = list;

for (; slow && fast && fast->next;)
{
slow = slow->next;
fast = fast->next->next;

if (slow == fast)
{
return (1);
}
}
return (0);
}
