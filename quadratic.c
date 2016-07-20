#include <stdio.h>
#include <math.h>

main() 
{
	double a, b, c, root1, root2;
	printf("Equation to solve for has the form ax^2 + bx + c = 0\n");
	printf("\nEnter value for a: ");
	scanf("%lf", &a);
	printf("\nEnter value for b: ");
	scanf("%lf", &b);
	printf("\nEnter value for c: ");
	scanf("%lf", &c);
	printf("\nEquation is %lf*x^2 + %lf*x + %lf", a, b, c);
	// check if a = 0
	if (a == 0)
	{
		double root = -c/b;
		printf("\nRoot is %lf\n", root);
	}
	else 
	{
		// check if real solutions
		if (sqrt(b*b - 4*a*c) >= 0) 
		{
			root1 = (0 - b + sqrt(b*b - 4*a*c))/(2*a);
			root2 = (0 - b - sqrt(b*b - 4*a*c))/(2*a);
			printf("\nFirst root is %lf", root1);
			printf("\nSecond root is %lf\n", root2);
		}
		else 
		{
			printf("\nImaginary roots.\n");
		}
	}
}
	
