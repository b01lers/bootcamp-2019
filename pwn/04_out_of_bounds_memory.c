#include <stdio.h>

void init()
{
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
}

int main()
{
    int target;
    char buff[80];

    target = 0x0A0B0C0D;
    init();

    printf("Welcome to basic memory corruption examples\n");
    printf("Send me your input: ");
    gets(buff);
    printf("\nCurrently target is: %#08x\n", target);

    if (target == 1068709651) {
        printf("You win!\n");
    } else {
        printf("Try again later\n");
    }
}
