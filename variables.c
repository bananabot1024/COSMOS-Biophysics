/* Program shows variable types and operations*/
#include <stdio.h>
#include <math.h>

main() 
{
	int i, j, k;
	double x, y, z;
	char s, t;
	i = 5;
	j = k = 8;
	x = 10.789;
	y = 1.2e6;
	z = x/y + 4*i;
	s = 'k';
	j = s; /* converts char to int*/
	k = i%2;
	printf("\n");
	printf("i = %d\n", i);
	printf("x = %lf\n", x);
	printf("y = %e\n", y);
	printf("z = %e\n", z);
	printf("s = %c\n", s);
	printf("k = %d\n", k);
}
