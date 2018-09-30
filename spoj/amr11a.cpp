//https://www.spoj.com/problems/AMR11A/

#include <bits/stdc++.h>
using namespace std;

#define INF 10000000
//TODO YET
int main() {

    ios::sync_with_stdio(0); 
    cin.tie();

    int testCases; cin >> testCases;

    while(testCases--){

        int rows, cols; cin >> rows >> cols;

        int mgrid[rows][cols], dp[rows][cols];

        //magic grid from input
        for(int r = 0; r < rows; r++){
            for(int c = 0; c < cols; c++){
                cin >> mgrid[r][c];
                dp[r][c] = -INF;
            }
        }

        //harry starts at (0, 0) in my 0 index notation
        mgrid[0][0] = mgrid[rows-1][cols-1] = 0;

        //GOAL: find maximum minimum strenght path
        //first column
        for(int r = 1; r < rows; r++){
            mgrid[r][0] = mgrid[r-1][0] - mgrid[r][0];
        }

        //first row
        for(int c = 1; c < cols; c++){
            mgrid[0][c] = mgrid[0][c-1] - mgrid[0][c];
        }

        //bottom-up approach maximizing strength path
        for(int r = 1; r < rows; r++){
            for(int c = 1; c < cols; c++){
                mgrid[r][c] = max(mgrid[r-1][c], mgrid[r][c-1]) - mgrid[r][c]; 
            }
        }

        //bottom-up approach
        for(int r = 1; r < rows; r++){
            for(int c = 1; c < cols; c++){
                mgrid[r][c] = max(mgrid[r-1][c], mgrid[r][c-1]) - mgrid[r][c]; 
            }
        }


        //bottom-up approach
        for(int r = 1; r < rows; r++){
            for(int c = 1; c < cols; c++){
                dp[r][c] = max(max(mgrid[r-1][c], mgrid[r][c-1]), dp[r][c]);
            }
        }

        // if(lowestStrength <= 0) cout << -lowestStrength + 1 << "\n";
        
        // else cout << "1" << "\n";

        cout << "MGRID" << endl;
        for(int i = 0; i < rows; i++){
            for(int j = 0; j < cols; j++)
                cout << " " << mgrid[i][j];

            cout << endl;
        }


        cout << "\nDP" << endl;
        for(int i = 0; i < rows; i++){
            for(int j = 0; j < cols; j++)
                cout << " " << dp[i][j];

            cout << endl;
        }

    }

}
