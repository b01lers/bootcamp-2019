#include <stdio.h>

void testFun()
{
    int check;
    printf("Check is %#x\n", check);
    if (check == 0xdeadbeef) {
        printf("You win!!!\n");
    } else {
        printf("Fail :(\n");
    }
}

void vulnFun()
{
    char buff[80];
    printf("Here's some space for you ;)");
    scanf("%100s", buff);
}

int main()
{
    vulnFun();
    testFun();
}
