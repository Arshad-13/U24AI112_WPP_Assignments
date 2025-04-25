#include <stdio.h>
#include <stdlib.h>
#include <string.h>
static int k=0;
void toh(int n, char a, char b, char c)
{
    k++;
    if (n == 0)
    {
        k--;
        return;
    }
    toh(n - 1, a, c, b);
    printf("Move disk %d from %c to %c\n", n, a, c);
    toh(n - 1, b, c,a);
}
int main()
{
    int n;
    scanf("%d", &n);
    toh(n, 'A', 'B', 'C');
    printf("%d",k);
    return 0;
}