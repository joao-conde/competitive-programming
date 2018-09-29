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

        int mgrid[rows][cols], dp[rows][cols]; //pair of current strength and lowest strength ever recorded through path

        //magic grid from input
        for(int r = 0; r < rows; r++){
            for(int c = 0; c < cols; c++){
                cin >> mgrid[r][c];
            }
        }

        //harry starts at (0, 0) in my 0 index notation
        mgrid[0][0] = mgrid[rows][cols] = dp[0][0] = 0;

        //GOAL: find maximum "strength" path but tracking HP lowest strength
        //first column
        for(int r = 1; r < rows; r++){
            pair<int, int> nextPair = mgrid[r][0];
            nextPair.first += mgrid[r-1][0].first;

            if(nextPair.first < mgrid[r][0].second)
                nextPair.second = nextPair.first;
            else
                nextPair.second = mgrid[r][0].second; 
        }

        //first row
        for(int c = 1; c < cols; c++){
            pair<int, int> nextPair = mgrid[0][c]; 
            nextPair.first += mgrid[0][c-1].first;

            if(nextPair.first < mgrid[0][c].second)
                nextPair.second = nextPair.first;
            else
                nextPair.second = mgrid[0][c].second; 
        }

        //bottom-up approach
        for(int r = 1; r < rows; r++){
            for(int c = 1; c < cols; c++){

                pair<int, int> maxLowerStrength;

                if(mgrid[r-1][c].second < mgrid[r][c-1].second)
                    maxLowerStrength = mgrid[r-1][c];
                else 
                    maxLowerStrength = mgrid[r][c-1];

                maxLowerStrength.first += mgrid[r][c].first;

                if(maxLowerStrength.first < maxLowerStrength.second)
                    maxLowerStrength.second = maxLowerStrength.first;

                mgrid[r][c] = maxLowerStrength;
            }
        }

        // if(lowestStrength <= 0) cout << -lowestStrength + 1 << "\n";
        
        // else cout << "1" << "\n";


        for(int i = 0; i < rows; i++){
            for(int j = 0; j < cols; j++)
                cout << " " << mgrid[i][j].second;

            cout << endl;
        }

    }

}
