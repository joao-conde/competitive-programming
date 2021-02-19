//https://www.spoj.com/problems/BEHAPPY/

#include <bits/stdc++.h>
using namespace std;

int memo[25][110]; //memo[girlfriend][gifts]

int solve(vector< pair<int, int> > &ranges, int girlfriend, int gifts){

    if(memo[girlfriend][gifts] != -1) return memo[girlfriend][gifts];

    if(girlfriend == ranges.size()){ //last girlfriend
        return (gifts == 0) ? 1 : 0;
    }

    //for every girlfriend find the number of ways by giving this girl a number of gifts i
    //such that i lies in the interval [ A[girlfriend] , B[girlfriend] ]
    int ways = 0;
    for(int i = ranges[girlfriend].first; i <= ranges[girlfriend].second; i++)
        ways += solve(ranges, girlfriend + 1, gifts - i);

    memo[girlfriend][gifts] = ways;

    return ways;
}

int main() {

    ios::sync_with_stdio(0);
    cin.tie();

    memset(memo, -1, sizeof(memo));

    while(true){

        int girlfriends, gifts;
        cin >> girlfriends >> gifts;
        if(girlfriends == 0 && gifts == 0)
            break;

        vector< pair<int, int> > ranges(girlfriends);
        for(int i = 0; i < girlfriends; i++){
            int ai, bi;
            cin >> ai >> bi;
            ranges[i] = make_pair(ai, bi);
        }

        solve(ranges, 0, gifts);
        cout << memo[0][gifts] << endl;
    }

}
