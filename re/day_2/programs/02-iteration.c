#include <stdio.h>
#include <stdlib.h>

/* By Rowan Hart - b01lers Capture The Flag Team */
/* Example 2 - Training Day 1 */

void static_while() {
	int i = 0;
	while (i < 10) {
		printf("STATIC WHILE ITERATING %d\n", i++);
	}
}

void static_for() {
	for (int i = 0; i < 10; i++) {
		printf("STATIC FOR ITERATING %d\n", i);
	}
}

void basic_while(int input) {
	int i = 0;
	while (i++ < input) {
		printf("WHILE - Iterating %d : %d\n", i, input);
	}
}

void basic_for(int input) {
	for (int i = 0; i < input; i++) {
		printf("FOR - Iterating %d : %d\n", i, input);
	}
}

void nested_for(int input) {
	for (int i = 0; i < input; i++) {
		for (int j = 0; j < input; j++) {
			printf("NESTED FOR - Iterating %d : %d\n", i, input);
		}
	}
}

int main(int argc, char ** argv) {
	int a;
	scanf("%d", &a);
	static_while();
	static_for();
	basic_while(a);
	basic_for(a);
	nested_for(a);
}
