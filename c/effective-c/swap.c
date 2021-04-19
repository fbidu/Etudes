/*
Because objects and functions are different things, object pointers and function
pointers are also different things, and should not be used interchangeably
*/
#include <stdio.h>
#include <stdlib.h>
int a() {
    return 10;
}

int main(void) {
    int x, z;
    int* x_addr, z_addr;
    x_addr = &x;
    z_addr = &z;
    
}
