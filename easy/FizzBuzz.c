#include <stdio.h>

int main(int argc, const char * argv[]) {
    FILE *file = fopen(argv[1], "r");
    unsigned int i, fizz, buzz, limit;

    while (fscanf(file, "%d %d %d", &fizz, &buzz, &limit) != EOF) {
        for (i = 1; i <= limit; i++) {
        	if (i % fizz == 0) {
        		printf("F");
        	}
        	if (i % buzz == 0) {
        		printf("B");
        	}
        	if (i % fizz != 0 && i % buzz != 0) {
        		printf("%d", i);
        	}
            if (i != limit) {
                printf(" ");
            }
        }
        printf("\n");
    }

    fclose(file);
    return 0;
}