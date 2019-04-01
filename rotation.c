/*rotates bodies of text by n character codes to check for ceaser cipher.
Best used with bash command 'for i in {0,n}; do cat ciphertext | ./a.out $i; done'*/

#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>
#define BUFFER 2000

int main(int argc, char *argv[]) {

	int i,c,rot;
	char s[BUFFER];

	int arg = strtol(argv[1], NULL, 10);

	for (i=0; i<BUFFER-1 && (c=getchar()) != EOF; ++i)	{
		c = tolower(c);
		if (c != '\n' && c != ' ')	{
			rot = c + arg;
			while (rot < 'a')	{
				rot = 'z' - ('a' - rot);
			}
			while (rot > 'z')	{
				rot = 'a' + (rot - 'z');
			}
			s[i] = rot;
		}
		else	{
			s[i] = c;
		}
	}

	s[i] = '\0';

	printf("%s\n", s);


	return 0;
}
