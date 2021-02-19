//https://www.spoj.com/problems/SHROOMS/

#include <bits/stdc++.h>
using namespace std;

#define INF 10000000

/* TIL:
*   1 - Binary search doing wonders again :D
*   2 - DP allows us to compute the most OPTIMAL PATH if at each step you can make the OPTIMAL CHOICE (not the case here)
*   3 - Solution: test each value in range of solutions with binary search, testing with dp
*/

int forest[501][501], dp[501][501];


bool isSolution(int shrooms, int rows, int cols){

    //lets assume we can start with these shrooms
    forest[0][0] = dp[0][0] = shrooms;

    for(int r = 0; r < rows; r++){
        dp[r][0] = dp[r-1][0] + forest[r][0];
        if(dp[r][0] < 0) dp[r][0] = -INF;
    }

    for(int c = 0; c < cols; c++){
        dp[0][c] = dp[0][c-1] + forest[0][c];
        if(dp[0][c] < 0) dp[0][c] = -INF; 
    }


    for(int r = 1; r < rows; r++){
        for(int c = 1; c < cols; c++){
            dp[r][c] = max(dp[r-1][c], dp[r][c-1]) + forest[r][c];
            if(dp[r][c] < 0) dp[r][c] = -INF;
        }
    }

    return dp[rows-1][cols-1] >= 0;
}


int main() {
    
    ios::sync_with_stdio(0); 
    cin.tie();


    int testCases;
    cin >> testCases;

    while(testCases--){

        int rows, cols, bsMax = 0;
        cin >> rows >> cols;

        for(int r = 0; r < rows; r++){
            for(int c = 0; c < cols; c++){
                cin >> forest[r][c];
                bsMax += abs(forest[r][c]);
            }
        }

        int lb = 0, ub = bsMax, mid;
        while(ub >= lb){

            mid = (lb + ub) / 2;

            if(isSolution(mid, rows, cols))
                ub = mid - 1;
            else
                lb = mid + 1;

        }

        cout << lb << "\n";
        
    }

}
