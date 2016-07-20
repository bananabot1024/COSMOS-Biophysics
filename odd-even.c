#include <stdio.h>
main() 
{
	int x, y, sum;
printf("\nEnter x: ");
scanf("%d", &x);
printf("Enter y: ");
scanf("%d", &y);
sum = x + y;
printf("the sum of x and y is %d \n", sum);
if (sum%2==1) printf("sum odd\n");
else printf("sum even\n");
}
