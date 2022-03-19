#include "func.cpp"
#include <math.h>

double func_cpp(long x, long y);

int main(){

    long x = pow(32432, 32);
    long y = pow(23423, 32);

    double result  = func_cpp(x, y);
    printf("%d", result);

}