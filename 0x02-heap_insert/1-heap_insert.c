#include <binary_trees.h>

/**
 * heap_insert - a function for inserting into a binary tree
 * based on the max heap ordering
 * @root: a double pointer to a root node
 * @value: the value to be inserted into the new node
 * Return: the address of the new node if successful
 */

heap_t *heap_insert(heap_t **root, int value)
{
	heap_t *new_node;
	heap_t *position = *root;
	
	if (root == NULL)
		return (NULL);

	if (*root == NULL)
		{
			new_node = binary_tree_node(NULL, value);
			*root = new_node;
			return(*root);
		}

	return(NULL)
}
