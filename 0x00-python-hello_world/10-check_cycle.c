#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to the head of the linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow_ptr = list;
	listint_t *fast_ptr = list;

	while (slow_ptr != NULL && fast_ptr != NULL && fast_ptr->next != NULL)
	{
		slow_ptr = slow_ptr->next;         /* Move slow_ptr by one */
		fast_ptr = fast_ptr->next->next;   /* Move fast_ptr by two */

		if (slow_ptr == fast_ptr)
			return (1);
	}

	return (0); /* No cycle found */
}
