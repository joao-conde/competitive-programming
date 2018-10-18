//https://www.spoj.com/problems/SKY/

#include <bits/stdc++.h>
using namespace std;

/* TIL:
*   1 - ...
*   2 - ...
*   3 - ...
*/

#define MAX_GRID_SIZE 1002
#define INF 100000

long long gridSize, xa, ya, xb, yb, a, b, c;

long long grid[MAX_GRID_SIZE][MAX_GRID_SIZE], dp[MAX_GRID_SIZE][MAX_GRID_SIZE];

long long getSkyscraperHeight(int i, int j){
    return (( (i-1) * gridSize + (j-1)) * a + b) % c;
}


long long getMoveCost(int h1, int h2){
    if(h1 <= h2) return 0;

    return abs(h1 - h2);
}


long long computeCostAndSetHeight(int x1, int y1, int x2, int y2){
    int cost = getMoveCost(grid[x1][y1], grid[x2][y2]);

    if(cost == 0)
        grid[x1][y1] = grid[x2][y2] = min(grid[x1][y1], grid[x2][y2]);
    
    return cost;
}



//test if val is a possible cost i.e any path does not cross that limit of operations
bool isSolution(int val){

    dp[xa][ya] = val;

    //first column
    for(int r = xa+1; r <= gridSize; r++){
        dp[r][ya] = dp[r-1][ya] - computeCostAndSetHeight(r-1, ya, r, ya);
        if(dp[r][ya] < 0) dp[r][ya] = -INF;
    }

    //first row
    for(int c = ya+1; c <= gridSize; c++){
        dp[xa][c] = dp[xa][c-1] - computeCostAndSetHeight(xa, c-1, xa, c);
        if(dp[xa][c] < 0) dp[xa][c] = -INF;
    }

    //bottom-up approach
    for(int r = xa+1; r <= gridSize; r++){
        for(int c = ya+1; c <= gridSize; c++){
            if(dp[r-1][c] >= dp[r][c-1]){
                dp[r][c] = dp[r-1][c] - computeCostAndSetHeight(r-1, c, r, c);
            }
            else{
                dp[r][c] = dp[r][c-1] - computeCostAndSetHeight(r, c-1, r, c);
            }

            if(dp[r][c] < 0) dp[r][c] = -INF;
        }
    }

    // for(int i = 0; i < gridSize+2; i++){
    //     for(int j = 0; j < gridSize+2; j++)
    //         cout << " " << dp[i][j];
    //     cout << endl;
    // }

    // cout << "DDDD: " << dp[xb-1][yb-1] << endl;
    return dp[xb-1][yb-1] > 0;

}


int main() {
    
    ios::sync_with_stdio(0); 
    cin.tie();

    cin >> gridSize >> xa >> ya >> xb >> yb >> a >> b >> c;

    //dont know what upper bound yet
    //ub = c + 100
    long long lb = 0, ub = 0, mid;
    
    //1-based indexes
    for(int i = 1; i <= gridSize; i++){
        for(int j = 1; j <= gridSize; j++){
            grid[i][j] = getSkyscraperHeight(i, j);
            ub += grid[i][j];
        }
    }

    while(ub >= lb){

        mid = (ub + lb) / 2;

        //cout << "\nTRYING BS VAL: " << mid << "\n";
        if(isSolution(mid)){
            ub = mid - 1;
        }
        else{
            lb = mid + 1;
        }

        cout << lb << "-" << mid << "-" << ub << "\n";

    }    


    cout << lb << "\n";

}
