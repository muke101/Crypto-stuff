#include <stdio.h>
#include <math.h>
#define BUFFER 90000

int main()
{
	unsigned long e,N;
	int nar[BUFFER], dar[BUFFER];
	double p, q, phiN;

	e = 3;
	N = 35;

	int ear[BUFFER];
	int quo, i;
	double r;

	quo = floor(e/N); 
	r = e % N;

	for (i=0; i<BUFFER-1 && r != 0; ++i)
	{
		e, N = N, r;
		quo = floor(e/N);
		r = e % N;
		ear[i] = quo;
	}
	ear[i] = '\0';

	int ni[BUFFER];
	int di[BUFFER];
	i = 0;

	ni[0] = ear[0];
	di[0] = 1;
	nar[0] = ni[0];
	dar[0] = di[0];
	ni[1] = ear[1]*ear[0]+1;
	di[1] = ear[1];
	nar[1] = ni[1];
	dar[1] = di[1];

	for (i=2; i<BUFFER-1 && ear[i] != '\0'; ++i)
	{
		ni[i] = ear[i]*nar[i-1]+nar[i-2];
		nar[i] = ni[i]; 
		di[i] = ear[i]*dar[i-1]+dar[i-2];
		dar[i] = di[i];
	}

	nar[i], dar[i] = '\0';
	e = 345754;
	int b;
	double root,square;
	for (i=0; nar[i] != '\0'; ++i)
	{
		phiN = floor((e*dar[i] - 1)/nar[i]);
		b = phiN - N - 1;
		square = pow(b,2);
		root = pow(square-4*N,0.5);
		p = (-b+root)/2;
		q = (-b-root)/2;;
		if (p*q == N)
		{
			printf("p: %f,\n q: %f\n", p, q);
			return 0;
		}
	}
	printf("nothing\n");
	return 0;
}