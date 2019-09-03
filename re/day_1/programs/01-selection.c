#include <stdio.h>
#include <stdlib.h>

/* By Rowan Hart - b01lers Capture The Flag Team */
/* Example 2 - Training Day 1 */

void basic_if(int input) {
	/* Basic IF Statements */
	if (input == 3) {
		printf("BASIC IF - Input was 3\n");
	}
	if (input == 5) {
		printf("BASIC IF - Input was 5\n");
	}
}

void if_else(int input) {
	/* If / Else statement */
	if (input == 10) {
		printf("IF / ELSE - Input was 10\n");
	} else {
		printf("IF / ELSE - Input was NOT 10\n");
	}
}

void elif(int input) {
	/* Multiple ElIf statements */
	if (input == 100) {
		printf("MULTIPLE ELIF - Input was 100\n");
	} else if (input == 101) {
		printf("MULTIPLE ELIF - Input was 101\n");
	} else if (input == 102) {
		printf("MULTIPLE ELIF - Input was 102\n");
	}
}

void switches(int input) {
	/* Switch Statements */
	switch(input) {
		case 1000: printf("SWITCH - Input was 1000\n"); break;
		case 1001: printf("SWITCH - Input was 1001\n"); break;
		case 1002: printf("SWITCH - Input was 1002\n"); break;
		case 1003: printf("SWITCH - Input was 1003\n"); break;
		case 2000: printf("SWITCH - Input was 2000\n");
		case 2001: printf("SWITCH - Input was 2001\n");
		case 2002: printf("SWITCH - Input was 2002\n");
		default: printf("SWITCH - Input was UNMATCHED\n"); break;
	}
}

int main(int argc, char ** argv) {
	if (argc != 2) {
		printf("Usage: 01-selection <int>\n");
		exit(1);
	}

	int input = atoi(argv[1]); /* Converts the string argument to an integer */
	basic_if(input);
	if_else(input);
	elif(input);
	switches(input);
}
