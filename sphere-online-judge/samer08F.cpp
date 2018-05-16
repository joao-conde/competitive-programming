#include <iostream>


using namespace std;


unsigned long long int feynman_squares(int n){
    return n*(n+1)*(2*n+1)/6;
}

int main(){


    int grid_size = -1;
    while(true){
        cin >> grid_size;
        if(grid_size == 0) break;
        cout << feynman_squares(grid_size) << endl;
    }


    return 0;
}