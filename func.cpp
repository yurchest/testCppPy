

extern "C"{
float func_cpp(float *x, int len){
    float sum = 0;
    for (int i = 0; i < len; i++){
		sum = sum +  x[i];
	}
    return (sum/len);
    }
}
