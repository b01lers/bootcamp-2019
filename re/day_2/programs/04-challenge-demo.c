#include <stdio.h>
#include <stdlib.h>

void validate(const char * input) {
	for (int i = 0; i < 9; i++) {
		if (input[i] > 'z' || input[i] < 'a') {
			exit(0);
		}
	}
	if (input[0] != 'x') {
		exit(0);
	}
	if (input[1] != 'y') {
		exit(0);
	}
	if (input[2] != 'l') {
		exit(0);
	}
	if (input[3] != 'o') {
		exit(0);
	}
	if (input[4] != 'p') {
		exit(0);
	}
	if (input[5] != 'h') {
		exit(0);
	}
	if (input[6] != 'o') {
		exit(0);
	}
	if (input[7] != 'n') {
		exit(0);
	}
	if (input[8] != 'e') {
		exit(0);
	}
	printf("Password correct!\n");
}

int main(int argc, char ** argv) {
	if (argc != 2) {
		printf("Error: 04-challenge-demo <password>\n");
		exit(0);
	}
	char * input = argv[1];
	validate(input);
	return 0;
}
