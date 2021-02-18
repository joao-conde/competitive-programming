//https://www.spoj.com/problems/BYTESM2/

#include <bits/stdc++.h>
using namespace std;


int main() {

    ios::sync_with_stdio(0); 
    cin.tie();

    int testCases; cin >> testCases;

    while(testCases--){

        int height, width;
        cin >> height >> width;

        int dp[height+1][width+1];

        vector< vector<int> > tileStones;
        for(int i = 0; i < height; i++){
            vector<int> rowStones;
            for(int j = 0; j < width; j++){
                int pstones; cin >> pstones;
                rowStones.push_back(pstones);
            }
            tileStones.push_back(rowStones);
        }

        //First row values are the stones present in the tiles
        for(int j = 0; j < width; j++){
            dp[0][j] = tileStones[0][j];
        }


        //bottom-up approach
        for(int i = 1; i < height; i++){
            for(int j = 0; j < width; j++){

                if(j == 0){ //no element backwards to the left
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j+1]);
                }
                else if(j == width - 1){ //no element backwards to the right
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]);
                }
                else{
                    dp[i][j] = max(dp[i-1][j], max(dp[i-1][j-1], dp[i-1][j+1]));
                }

                //previous stones + current tile ones
                dp[i][j] += tileStones[i][j];
            }
        }

        int max = -1;

        for(int j = 0; j < width; j++){
            if(dp[height - 1][j] > max) max = dp[height - 1][j];
        }

        cout << max << endl;
    }
}
