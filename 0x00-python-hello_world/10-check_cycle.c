#include "lists.h"

/**
 * check_cycle - entry point
 * Description: check loop for linked list
 * @list: * linked list
 * Return: 0 if no 1 if exists
 */
int check_cycle(listint_t *list)
{
	const listint_t *listone = NULL, *listwo = NULL;


	if (list == NULL)
		return (0);

	listone = list;
	listwo = list;

	while (listone && listwo && listwo->next)
	{
		listone = listone->next;
		listwo = listwo->next->next;
		if (listone == listwo)
			return (1);
	}
	return (0);
}
