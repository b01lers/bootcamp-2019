#include <stdio.h>

void init()
{
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
}

int main()
{
    struct {
        char a;
        char b[20];
        char c;
    } foo;

    foo.a = foo.c = 0;

    for (int i = -1; i < 21; i++) {
        foo.b[i] = i;
        printf("%d, %d, %d, %d\n", i, foo.a, foo.b[i], foo.c);
    }
}
