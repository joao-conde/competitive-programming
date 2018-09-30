//https://www.spoj.com/problems/AMR11A/

#include <bits/stdc++.h>
using namespace std;

#define INF 1000000000


/* TIL:
*   1 - Binary search doing wonders again :D
*   2 - DP allows us to compute the most OPTIMAL PATH if at each step you can make the OPTIMAL CHOICE (not the case here)
*/

int dp[501][501], mgrid[501][501];

bool isSolution(int val, int rows, int cols){

    //lets assume we can start with val strength on HP
    mgrid[0][0] = dp[0][0] = val;

    //first column
    for(int r = 0; r < rows; r++){
        dp[r][0] = dp[r-1][0] + mgrid[r][0];

        //if we 'die' (hit 0 or less strength) then this path does not satisfy us
        //so we give it -INF and later on opt for high strength paths
        if(dp[r][0] <= 0) dp[r][0] = -INF;
    }


    //first row (IDENTICAL TO COLUMN)
    for(int c = 0; c < cols; c++){
        dp[0][c] = dp[0][c-1] + mgrid[0][c];
        if(dp[0][c] <= 0) dp[0][c] = -INF;
    }

    //bottom-up approach
    for(int r = 1; r < rows; r++){
        for(int c = 1; c < cols; c++){
            //looking for maximum strength path
            dp[r][c] = max(dp[r-1][c], dp[r][c-1]) + mgrid[r][c];
            if(dp[r][c] <= 0) dp[r][c] = -INF;
        }
    }


    //val is a solution if in the end we have more than 0 strength
    return dp[rows-1][cols-1] > 0;
}


int main() {

    ios::sync_with_stdio(0); 
    cin.tie();

    int testCases; cin >> testCases;

    while(testCases--){

        int rows, cols, transverseEntireGrid = 0; 
        cin >> rows >> cols;

        //magic grid from input
        for(int r = 0; r < rows; r++){
            for(int c = 0; c < cols; c++){
                cin >> mgrid[r][c];
                transverseEntireGrid += abs(mgrid[r][c]); 
            }
        }


        //binary search: trying possible starting values
        int lb = 1, ub = transverseEntireGrid, mid;
        while(ub >= lb){

            mid = (lb + ub) / 2;

            if(isSolution(mid, rows, cols)){
                ub = mid - 1;
            }
            else{
                lb = mid + 1;
            }

        }

        cout << lb << "\n";

    }

}
