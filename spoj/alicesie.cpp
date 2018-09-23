//https://www.spoj.com/problems/ALICESIE/

#include <bits/stdc++.h>
using namespace std;

int computeNumberOfProperDivisors(int n){

    int properDivisors = 0, sqrt_n = ceil(sqrt(n));
    
    for(int i = 0; i < sqrt_n; i++){
        if(n % i == 0)  properDivisors++;
    }

    return properDivisors;
}


int main() {
    
    ios::sync_with_stdio(0); 
    cin.tie();

    int testCases; cin >> testCases;

    while(testCases--){
        int n; cin >> n;
        cout << n - computeNumberOfProperDivisors(n) << "\n";
    }

}
