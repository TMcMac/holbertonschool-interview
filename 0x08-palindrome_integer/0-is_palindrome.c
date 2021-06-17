#include "palindrome.h"

/**
 * is_palindrome - see if a int is a palindrome
 * @n: a long int
 * Return: 1 if true, 0 if false
 */

int is_palindrome(unsigned long n)
{
  unsigned long num = n;
  unsigned long mun = 0;
  int remainder;

  if (n < 10)
    return (1);

  while (num != 0)
    {
      remainder = (num % 10);
      mun = (mun * 10) + remainder;
      num /= 10;
    }

  if (mun == n)
    return (1);
  else
    return (0);
}
