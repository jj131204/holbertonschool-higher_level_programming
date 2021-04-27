#include "lists.h"

/**
 *check_cycle - prototype
 *
 *@list: pointer to cycle.
 *
 *Return: 0 or 1
 */

int check_cycle(listint_t *list)
{
	listint_t *l = list;

	if (!list)
		return (0);

	while (list && l)
	{
		l = l->next->next;
		list = list->next;
		if (list == l)
		{
			return (1);
		}
	}

return (0);
}
