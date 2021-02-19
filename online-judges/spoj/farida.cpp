//https://www.spoj.com/problems/FARIDA/

#include <bits/stdc++.h>
using namespace std;

/* TIL:
 *   1 - Adding non-adjavent values can at first seem to sum all values alternating or jumping 1 by 1
 *    which is incorrect
 *
 *   2 - It is considered dynamic programming because we are using memoization in the sense we compute
 *    new values based on previous computed ones
 */

/*
 *    Computes maximum possible sum of non-adjacent values in an array 'vals' of size 'size'.
 *    From www.geeksforgeeks.org/maximum-sum-such-that-no-two-elements-are-adjacent/
 */

long long nonAdjacentSum(int vals[], int size){

    if(size <= 0) return 0;

    long long incl, excl_aux, excl = 0;

    incl = vals[0];

    for(int i = 1; i < size; i++){

        /* current max excluding i */
        excl_aux = max(incl, excl);

        /* current max including i */
         incl = excl + vals[i];
         excl = excl_aux;

    }

    return max(incl, excl);
}


int main() {
    ios::sync_with_stdio(0);
    cin.tie();

    int testCases, size, dummy;
    cin >> testCases;

    for(int j = 0; j < testCases; j++){

        cin >> size;

        int coins[size];

        for(int i = 0; i < size; i++){
            cin >> dummy;
            coins[i] = dummy;
        }

        cout << "Case " << j+1 << ": " << nonAdjacentSum(coins, size) << "\n";

    }
}
