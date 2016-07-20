#include <stdio.h>
main() 
{
	int j;
	// print first 20 ints
	for (j = 1; j <= 20; j++) {
		printf("%d ", j);	
	}
	printf("\n");

	// print all except odd between 3 and 20
	for (j = 4; j < 20; j++) {
		if (j % 2 == 0) printf("%d ", j);	
	}
	printf("\n");

	// print all even between 1 and 50 except mod 12
	for (j = 2; j <= 50; j+=2) {
		if (j % 12 != 0) printf("%d ", j);		
	}
	printf("\n");

}
