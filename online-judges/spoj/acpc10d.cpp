//https://www.spoj.com/problems/ACPC10D/

#include <bits/stdc++.h>
using namespace std;

#define TRI_GRAPH_COLS 3
#define INF 100000000

int main() {

    ios::sync_with_stdio(0);
    cin.tie();

    int testNo = 1;
    while(true){

        int rows; cin >> rows;
        if(rows == 0) break;

        //node costs from input
        vector< vector<int> > costs(rows);
        for(int i = 0; i < rows; i++){
            vector<int> row(TRI_GRAPH_COLS);

            for(int j = 0; j < TRI_GRAPH_COLS; j++) cin >> row[j];

            costs[i] = row;
        }

        int dp[rows][TRI_GRAPH_COLS];

        dp[0][0] = INF; //forces left node to be ignored due to high value
        dp[0][1] = costs[0][1]; //middle node has node weight (starting point)
        dp[0][2] = costs[0][2] + dp[0][1]; //right node is picked if his own weight plus first node (middle one) is low, happens when right node cost is negative

        //bottom-up approach
        for(int row = 1; row < rows; row++){

            //node 0 possible inc paths from above and upper-right node
            dp[row][0] = min(dp[row - 1][0], dp[row - 1][1]) + costs[row][0];

            //node 1 possible inc paths from above or left node
            dp[row][1] = min(min(dp[row - 1][1], min(dp[row - 1][0], dp[row - 1][2])), dp[row][0]) + costs[row][1];

            //node 2 possible inc paths from above, upper-left node or from left node
            dp[row][2] = min(min(dp[row - 1][2], dp[row - 1][1]), dp[row][1]) + costs[row][2];

        }

        //printing smallest cost path to middle bottom node
        cout << testNo << ". " << dp[rows-1][1] << endl;
        testNo++;
    }

}
