#include "func.cpp"
#include <iostream>





float func_cpp(float, unsigned long long &);

using namespace std;

int main(){

    float array[] {1.0, 2.0, 3.0, 4.0, 5.0};
//    printf("%f\n\n", array[2]);
//    printf("%d\n\n", sizeof(array) / sizeof(float));
    unsigned long long len = 5;
    printf("%f\n\n", func_cpp(array, len));
    printf("%x\n\n", &len);

    return 0;
}
