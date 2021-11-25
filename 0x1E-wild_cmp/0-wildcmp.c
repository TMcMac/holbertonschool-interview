#include "holberton.h"
/**
 * wildcmp - a function to compare two strings to
 * determin if they are exactly the same. A string
 * can contain a wild card that is equal to any char
 * in any quantity, so 'hello' and 'h*o' are considered
 * as exact matches.
 * @s1: a string
 * @s2: a string that can contain the wildcard *
 * Return: 1 if exactly the same, 0 if not
 */
int wildcmp(char *s1, char *s2)
{
 	/* If we hit the end of both strings, they match */
	if (*s1 == '\0' && *s2 == '\0')
		return (1);
	/* If we hit the end of s1 but !s2 we need to check for chars */
	if (*s1 == '\0' && *s2 == '*')
		return (wildcmp(s1, s2 + 1));
	/* If we have same char in s1/s2 they match adv both */
	if (*s1 == *s2)
		return (wildcmp(s1 + 1, s2 + 1));
	/* If s2 is on a wildcard we check for both the next in s1 and s2 */
	if (*s2 == '*')
		return (wildcmp(s1, s2 + 1) || wildcmp(s1 + 1, s2));

	return (0);
}
