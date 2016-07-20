/* add 2 numbers*/
/* pre-processor statement to use the standard i/o library*/
#include <stdio.h>

int main() 
{
    int a, b, sum;

    printf("Enter the first number: ");
    scanf("%d", &a);
    printf("\nEnter the second number: ");
    scanf("%d", &b);
    sum = a + b;
    printf("\nThe sum of the two numbers is %d", sum);
    printf("\n");

}
