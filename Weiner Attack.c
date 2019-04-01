#include <stdio.h>
#include <math.h>
#define BUFFER 9000

int * cfExpansion(int n, int d)
{
	int e[BUFFER];
	int q, i;
	double r;

	q = floor(n/d); 
	r = n % d;

	for (i=0; i<BUFFER-1 && r != 0; ++i)
	{
		n, d = d, r;
		q = floor(n/d);
		r = n % d;
		e[i] = q;
	}
	e[i] = '\0';
	return e;
}

void convergents(int *e, int *nar, int *dar)
{
	int ni[BUFFER];
	int di[BUFFER];
	int i;

	ni[0] = *e;
	di[0] = 1;
	*nar = ni[0];
	*dar = di[0];
	ni[1] = *(e+1)*(*e)+1;
	di[1] = *(e+1);
	*(nar+1) = ni[1];
	*(dar+1) = di[1];

	for (i=2; i<BUFFER-1 && *(e+i) != '\0'; ++i)
	{
		ni[i] = *(e+i)*(*(nar+(i-1)))+*(nar+(i-2));
		*(nar+i) = ni[i]; 
		di[i] = e[i]*(*(dar+(i-1)))+*(dar+(i-2));
		*(dar+i) = di[i];
	}

	*(nar+i), *(dar+i) = '\0';
}

void quadraticEquation(int a, int b, int c, int *root1, int *root2)
{
	*root1 = (-b+pow(pow(b,2)-4*a*c,0.5))/2*a;
	*root2 = (-b-pow(pow(b,2)-4*a*c,0.5))/2*a;
}

int main()
{
	unsigned long e,N;
	int *continuedFractions;
	int *nar[BUFFER], *dar[BUFFER];
	double p, q, phiN;

	e = 345754;
	N = 4547457376;

	continuedFractions = cfExpansion(e, N);
	convergents(*continuedFractions, &nar, &dar);

	for (int i=0; *(nar+i) != '\0'; ++i)
	{
		phiN = floor((e*(*(dar+i)) - 1)/(*(nar+i)));
		quadraticEquation(1,(phiN - N - 1), N, &p, &q);
		if (p*q == N)
		{
			printf("p: %d,\n q: %d\n", p, q);
			return 0;
		}
	}

	return 0;
}