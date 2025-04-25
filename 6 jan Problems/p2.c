#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void stock_span(int* prices, int days, int* spans) 
{
    for (int i = 0; i < days; i++) 
    {
        int span = 1;
        
        int j = i - 1;
        
        while (j >= 0 && prices[i] >= prices[j]) 
        {
            span++;
            j--;
        }
        
        spans[i] = span;
    }
}

int main() {
    int days;

    printf("Enter the number of days: ");
    scanf("%d", &days);

    int *prices = (int*)malloc(days * sizeof(int));
    int *spans = (int*)malloc(days * sizeof(int));
   
    for (int i = 0; i < days; i++) 
    {
        printf("Enter the price of day %d: ", i);
        scanf("%d", &prices[i]);
    }
    
    stock_span(prices, days, spans);
    
    printf("\nThe span of the stock prices is: ");
    for (int i = 0; i < days; i++) {
        printf("%d ", spans[i]);
    }
    printf("\n");

    free(prices);
    free(spans);
    
    return 0;
}