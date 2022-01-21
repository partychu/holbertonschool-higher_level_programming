#include "lists.h"

/**
 * check_cycle
 * @list: list to check
 *
 * Return: return 0 for no cycle, 1 for cycle
 *
 */

int check_cycle(listint_t *list)
{
	listint_t *p1 = list;
	listint_t *p2 = list;

	while (p2->next != NULL && p2->next->next != NULL)
	{
		p1 = p1->next;
		p2 = p2->next->next;
		if (p1 == p2)
			return (1);
	}
	return (0);
}
