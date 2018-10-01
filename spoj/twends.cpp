//https://www.spoj.com/problems/TWENDS/

#include <bits/stdc++.h>
using namespace std;


int cards[1005], memo[1005][1005];

int computeSmartMaxPts(int lidx, int ridx){

    if(lidx > ridx) return 0;

    if(memo[lidx][ridx] != -1) return memo[lidx][ridx];

    int pts, takeLeft, takeRight;

    if(memo[lidx+1][ridx] != -1)
        takeLeft = memo[lidx+1][ridx];
    else
        takeLeft = computeSmartMaxPts(lidx+1, ridx);

    if(memo[lidx][ridx-1] != -1)
        takeRight = memo[lidx][ridx-1];
    else
        takeRight = computeSmartMaxPts(lidx, ridx-1);

    if(takeLeft + cards[lidx] >= takeRight + cards[ridx]){
        pts = cards[lidx];
        lidx++;
    }
    else{
        pts = cards[ridx];
        ridx--;
    }

    //dumb greedy pick
    if(cards[lidx] >= cards[ridx])
        lidx++;
    else   
        ridx--;


    if(memo[lidx][ridx] != -1) return memo[lidx][ridx] + pts;

    memo[lidx][ridx] = computeSmartMaxPts(lidx, ridx);
    return memo[lidx][ridx] + pts;
}

int main(){
    
    ios::sync_with_stdio(0); 
    cin.tie();


    int n, game = 1;
    while(cin >> n){

        if(n == 0) break;

        memset(memo, -1, sizeof(memo));

        int total = 0;
        for(int i = 0; i < n; i++){
            int pts; cin >> pts;
            total += pts;
            cards[i] = pts;
        }

        //from total = smart + greedy and smart - greedy = diff
        //diff = 2 * smart - total
        cout << "In game " << game << ", the greedy strategy might lose by as many as " << abs(2 * computeSmartMaxPts(0, n) - total) << " points.\n";
        game++;
    }

}
