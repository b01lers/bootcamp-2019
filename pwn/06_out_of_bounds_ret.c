#include <stdio.h>

void init()
{
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
}

void win ()
{
    printf("You win!\n");
}

void fail()
{
    printf("Sorry, you fail\n");
}

int main()
{
    char buff[80];

    init();
    printf("Welcome to basic memory corruption examples\n");
    printf("Send me your input: ");
    gets(buff);

    fail();
    return 0;
}
