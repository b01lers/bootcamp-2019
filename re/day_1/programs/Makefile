CC=gcc
32FLAGS=-m32
CFLAGS=-g -O0

all: 00-hello-world 01-selection 02-iteration 03-function-calls-returns

00-hello-world:
	$(CC) -o 00-hello-world 00-hello-world.c $(CFLAGS)
	$(CC) -o 00-hello-world-32 00-hello-world.c $(CFLAGS) $(32FLAGS)

01-selection:
	$(CC) -o 01-selection 01-selection.c $(CFLAGS)
	$(CC) -o 01-selection-32 01-selection.c $(CFLAGS) $(32FLAGS)

02-iteration:
	$(CC) -o 02-iteration 02-iteration.c $(CFLAGS)
	$(CC) -o 02-iteration-32 02-iteration.c $(CFLAGS) $(32FLAGS)

03-function-calls-returns:
	$(CC) -o 03-function-calls-returns 03-function-calls-returns.c $(CFLAGS)
	$(CC) -o 03-function-calls-returns-32 03-function-calls-returns.c $(CFLAGS) $(32FLAGS)

.PHONY: clean
clean:
	rm 00-hello-world
	rm 00-hello-world-32
	rm 01-selection
	rm 01-selection-32
	rm 02-iteration
	rm 02-iteration-32
	rm 03-function-calls-returns
	rm 03-function-calls-returns-32

