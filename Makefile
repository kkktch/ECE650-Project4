CC=g++
CFLAGS=-O3
EXTRAFLAGS=-lpqxx -lpq

all: test

test: main.cpp 
	$(CC) $(CFLAGS) -o test main.cpp $(EXTRAFLAGS)

clean:
	rm -f *~ *.o test

clobber:
	rm -f *~ *.o
