CC = gcc
CFLAGS = -O3 -std=c11 -Wall -Wextra -Werror
LDLIBS = -l:liblapack.so.3 -l:libblas.so.3 -lm

.PHONY: all clean
all: build/finite_checks build/physics4d

build:
	mkdir -p build

build/finite_checks: scripts/finite_checks.c | build
	$(CC) $(CFLAGS) $< $(LDLIBS) -o $@

build/physics4d: scripts/physics4d.c | build
	$(CC) $(CFLAGS) $< $(LDLIBS) -o $@

clean:
	rm -f build/finite_checks build/physics4d
