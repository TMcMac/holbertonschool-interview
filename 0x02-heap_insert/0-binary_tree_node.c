#include "binary_trees.h"

/**
 * binary_tree_node - is a punction to create a new node and insert
 * it under the supplied partent
 * @parent: a node in a binary tree
 * @value: a int value to be added to the new node
 * Return: the address to the new node, or null for any failure
 */

binary_tree_t *binary_tree_node(binary_tree_t *parent, int value)
{
	binary_tree_t *new_node = malloc(sizeof(binary_tree_t) * 1);

	if (new_node == NULL)
	  	return (NULL);

	new_node->n = value;
	new_node->left = NULL;
	new_node->right = NULL;
	new_node->parent = parent;

	return (new_node);
}
