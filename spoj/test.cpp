//http://www.spoj.com/problems/TEST/

#include <cstdio>
#include <iostream>

using namespace std;

int main(){

    int n = 0;

    while(true){
        cin >> n;
        
        if(n == 42) break; 

        printf("%d\n", n);
    }

    return 0;
}