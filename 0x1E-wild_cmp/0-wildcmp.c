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
	int s1len, s2len;

	/* if either string is null or empty it's game over */
	if (s1 == NULL || s2 == NULL)
		return (0);
	s1len = _strlen(s1);
	s2len = _strlen(s2);
	if (s1len == 0 || s2len == 0)
		return (0);

	/* Quick check of first and last positions */
	/* if s2 is just an * it will match any s1 */
	if (s1[0] != s2[0] && s2[0] != '*')
		return (0);
	else if (s2len == 1 && s2[0] == '*')
		return (1);
	else if (allstar(s2, s2len))
		return (1);
	else if (s1[s1len] != s2[s2len] && s2[s2len] != '*')
		return (0);

	check = full_check(s1, s2);
	return (check);
}


/**
 * _strlen - a function to get the len of a string
 * @string: a pointer to the start of a string
 * Return: an int for length
 */
int _strlen(char *string)
{
	int count = 0;

	while (string[count] != '\0')
		count++;
	return (count);
}


/**
 * allstar - a check of if a string is all ***
 * @string: a string, a pointer to a string
 * @strlen: length of the string
 * Return: 1 if all starts, 0 if not
 */
int allstar(char *string, int strlen)
{
	int i;

	for (i = 0; i < strlen; i++)
	{
		if (string[i] != '*')
			return (0);
	}
	return (1);
}


/**
 * full_check - do a full check of the strings
 * @s1: a string
 * @s2: a string that may contain wildcards '*'
 * Return: 1 for full match, 0 for not
 */


int full_check(char *s1, char *s2)
{
	/* If we hit the end of both strings, they match */
	if (*s1 == '\0' && *s2 == '\0')
		return (1);
	/* If we hit the end of s1 but !s2 we need to check for chars */
	if (*s1 == '\0' && *s2 == '*')
		return (full_check(s1, s2 + 1));
	/* If we have same char in s1/s2 they match adv both */
	if (*s1 == *s2)
		return (full_check(s1 + 1, s2 + 1));
	/* If s2 is on a wildcard we check for both the next in s1 and s2 */
	if (*s2 == '*')
		return (full_check(s1, s2 + 1) || full_check(s1 + 1, s2));

	return (0);
}
