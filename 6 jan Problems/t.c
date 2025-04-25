// codebooks stock span

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    int days;

    printf("Enter the number of days: ");
    scanf("%d", &days);

    int price[days];

    for(int i=0; i<days; i++)
    {
        printf("Enter the price of day %d: ", i);
        scanf("%d", &price[i]);
    }

    int span=1;
    int si[days];

    for(int i=0; i < days; i++)
    {
        if(price[i] > price[i-1])
        {
            si[i] = span;
            span++;
        }
        else
        {
            span=1;
            si[i] = span;
            
        }
    }

    printf("\nThe span of the stock prices is: ");
    for(int i= 0 ; i< days; i++)
    {
        printf("%d ", si[i]);
    }
    return 0;
}