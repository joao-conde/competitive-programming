//https://www.spoj.com/problems/BEHAPPY/

#include <bits/stdc++.h>
using namespace std;


int solve(vector< pair<int, int> > &ranges, int girlfriend, int gifts){

    //no more gifts left to give
    if(gifts < 0) return 0;
    
    //only one girlfriend (index 0)
    if(girlfriend == 0)
        return (gifts >= ranges[girlfriend].first && gifts <= ranges[girlfriend].second) ? 1 : 0;
    

    //for every girlfriend find the number of ways by giving this girl a number of gifts i 
    //such that i lies in the interval [ A[girlfriend] , B[girlfriend] ]
    int ways = 0;
    for(int i = ranges[girlfriend].first; i <= ranges[girlfriend].second; i++)
        ways += solve(ranges, girlfriend-1, gifts-i);

    return ways;
}

int main() {

    ios::sync_with_stdio(0); 
    cin.tie();

    int girlfriends, gifts;
    while(true){

        cin >> girlfriends >> gifts;
        if(girlfriends == 0 && gifts == 0)
            break;

        vector< pair<int, int> > ranges(girlfriends); 
        for(int i = 0; i < girlfriends; i++){
            int ai, bi; 
            cin >> ai >> bi;
            ranges[i] = make_pair(ai, bi);
        }

        cout << solve(ranges, girlfriends-1, gifts) << endl;
    }

}
