//https://www.spoj.com/problems/COINS/

#include <bits/stdc++.h>
using namespace std;

/* TIL:
*   1 - If input too large we can use part memoization and part pure recursion, using stack space and memory
*/

#define MAX 100000000 //10^8


long long memo[MAX];

long long computeDollarValue(long long byteCoin){

    if(byteCoin == 0) return 0;

    //memoization of values up untill MAX
    if(byteCoin <= MAX){
        
        if(memo[byteCoin] != -1) 
            return memo[byteCoin];
        else
            return memo[byteCoin] = max(byteCoin, computeDollarValue(byteCoin / 2) + computeDollarValue(byteCoin / 3) + computeDollarValue(byteCoin / 4));

    }

    return max(byteCoin, computeDollarValue(byteCoin / 2) + computeDollarValue(byteCoin / 3) + computeDollarValue(byteCoin / 4));
}


int main() {
    
    ios::sync_with_stdio(0); 
    cin.tie();

    int byteCoins;
    while(cin >> byteCoins){
        memset(memo, -1, sizeof(memo));
        cout << computeDollarValue(byteCoins) << endl;
    }
    
}
