#include <stdio.h>

main()
{
	double time, rate, distance;
    rate = 14;
    printf("Enter next time: ");
    scanf("%lf", &time);
    while (time > 0)
    {
        distance = rate * time;
        printf("Time = %lf hours\n", time);
        printf("Distance = %lf km\n", distance);
        printf("Enter next time: ");
        scanf("%lf", &time);
    }

}
