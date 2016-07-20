#include <stdio.h>
main()
{
	int i, j, value;
	for (i = 1; i < 4; i++) {
		for (j = 1; j < 5; j++) {
			value = i + 2*j;
			printf("%d\n", value);
		}
	}
}
