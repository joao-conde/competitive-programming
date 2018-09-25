//https://www.spoj.com/problems/UOFTAE/

#include <bits/stdc++.h>
using namespace std;


long long memo[205][205]; //memo[foxlings][crackers]

long long distribute(vector<long long> &a, vector<long long> &b, long long foxlings, long long crackers){

    if(memo[foxlings][crackers] != -1) return memo[foxlings][crackers];

    if(foxlings == a.size()){ //last foxen
        return (crackers == 0) ? 1 : 0;
    }

    long long ways = 0;
    for(int i = a[foxlings]; i <= b[foxlings]; i++){
        ways += distribute(a, b, foxlings + 1, crackers - 1);
    }

    memo[foxlings][crackers] = ways;
    return ways;
}

int main() {

    ios::sync_with_stdio(0); 
    cin.tie();

    memset(memo, -1, sizeof(memo));

    int testCases; cin >> testCases;
    while(testCases--){

        long long foxlings, crackers;
        cin >> foxlings >> crackers;

        vector<long long> a(foxlings), b(foxlings);
        for(int i = 0; i < foxlings; i++){
            cin >> a[i];
            cin >> b[i];
        }

        distribute(a, b, 0, crackers);

        cout << memo[0][crackers] % 1000000007 << endl;
    }
}
