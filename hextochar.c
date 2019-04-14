#include <stdio.h>
#include <ctype.h>
#include <math.h>
#define BUFFER 1000


int ctoi(char c) //take character string of hex number and convert each number into it's respective integer
{
	if (isdigit(c))
		return c - '0';
	else
		return 10 + ((tolower(c) - '0') - 49); //ASCII value of 'a' is 49, 'b' 50 etc
}

int main()	{
	int i, j, c, n=0;
	char s[BUFFER];
	int inNumber = 0;

	for (i=0; i<BUFFER && (c=getchar()) != EOF; ++i)
		s[i] = c;

	for (j=0; j != i; ++j)	{
		if (s[j] != ' ')	{
			if (inNumber == 0) 	{
				inNumber = 1;
				n = ctoi(s[j])*16;
			}
			else	{
				n = n + ctoi(s[j]);
			}
		}
		else 	{
			inNumber = 0;
			printf("%c",n);
			n = 0;
		}
	}

	printf("%c\n");

	return 0;
}
