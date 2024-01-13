#include <iostream>

using namespace std;

/*
    Doesn't work in a macosx for some reason
    ios::sync_with_stdio(0);
    cin.tie(0);
*/

/*

    g++ -o io_out in_out.cpp
    ./io_out

*/

int main() {
    int a, b;
    string s;

    cin >> a >> b;
    cout << a << " " << b;

    // we can read a string cout, but it cannot have space
    // hence to be able to read a string as a whole we will use the following technique.
    
    cout << "\nEnter a string of your choice \n";
    getline(cin, s);

    cout << s << endl;
}
