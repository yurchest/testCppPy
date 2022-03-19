#include <iostream>


extern "C" double func_cpp(const double* x, size_t len){
    double sum = 0;
    for (int i = 0; i < len; i++){
//        printf("SUM = %f\n", sum);
		sum = sum +  x[i];
	}
//	x[0] = 2224;
//    printf("SUM = %.200f", sum);

//    printf("  In cpp : int  %f  return %f\n", x[0],  res);
    return (sum / len);
}
