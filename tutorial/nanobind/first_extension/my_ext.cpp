#include <nanobind/nanobind.h>
#include <cmath>

// Testing a add function
int add(int a, int b) { return a+b; }

// Testing a greet function
char* say_hello(const char* msg) { 
    const char *greet = "Hello, ";
    char *ptr = (char*) malloc(strlen(msg) + strlen(greet) +  1);

    strcpy(ptr, greet); // copy direction R to L
    strcat(ptr, msg);   // concat R to L
    return ptr; 
}

// get sqrt - we can also test how fast it is in C++ over Python
double squareRoot(double x) {
    return sqrt(x);
}

NB_MODULE(my_ext, m) {
    m.def("add", &add);
    m.def("msg", &say_hello);
    m.def("sqrt", &squareRoot);
}