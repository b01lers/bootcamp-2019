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
    void (*target)();
    char buff[80];

    target = &fail;
    init();

    printf("Welcome to basic memory corruption examples\n");
    printf("Send me your input: ");
    gets(buff);
    printf("\nCurrently target is: %p\n",  target);

    target();
}
