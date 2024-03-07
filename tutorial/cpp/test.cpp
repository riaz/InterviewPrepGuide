#include <iostream>
#include <tuple>

using namespace std;


tuple<int, int, int> go(int num) {
    return {num, num+1, num+2};
}

int s(int num) {
    auto [x,y,z] = go(num);
    return y;
}

// Run: g++ -std=c++17 test.cpp
// a.out
int main(){
    int num = 10;
    cout << s(num) << endl;
    return 0;
}

