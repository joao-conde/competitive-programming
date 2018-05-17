//http://www.spoj.com/problems/AE00/

#include <iostream>
#include <cmath>

using namespace std;


unsigned long long byteman(int squares){
 
    unsigned long long rectangles = 0;

    if(squares == 1) return 1;

    //count up to sqrt(n) evalute which divides evenly = +1 solution
    int sqrt_n = sqrt(squares);
    for(int i = 1; i <= sqrt_n; i++)
        if(squares % i == 0) rectangles++;
    
    
    //call for n-1
    rectangles += byteman(squares-1);

    return rectangles;
}


int main(){

    int squares = 0;
    cin >> squares;

    cout << byteman(squares) << endl;

    return 0;
}