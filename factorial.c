#include <stdio.h>

main() 
{
	int a, factorial = 1;	
	printf("enter a number: ");
	scanf("%d", &a);
	int i;
	for (i = 1; i <= a; i++) factorial *= i;
	printf("factorial: %d\n", factorial);
	
}
