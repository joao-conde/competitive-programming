//https://www.spoj.com/problems/ALICESIE/

#include <bits/stdc++.h>
using namespace std;


int main() {

    ios::sync_with_stdio(0);
    cin.tie();

    int testCases; cin >> testCases;

    while(testCases--){
        int n; cin >> n;

        /*
         * From simple pattern observation comes that for:
         *  - odd numbers: unmarked = ceil(n/2) or (n+1)/2
         *  - even numbers: unmarked = n/2
         */

        if(n % 2 == 0)
            cout << n/2 << "\n";
        else
            cout << (n+1)/2 << "\n";
    }

}
