//https://www.spoj.com/problems/AMR11A/

#include <bits/stdc++.h>
using namespace std;

#define INF 100000

int main() {

    ios::sync_with_stdio(0); 
    cin.tie();

    int testCases; cin >> testCases;

    while(testCases--){

        int rows, cols; cin >> rows >> cols;
        int mgrid[rows][cols];

        //magic grid from input
        for(int r = 0; r < rows; r++){
            for(int c = 0; c < cols; c++){
                cin >> mgrid[r][c];
            }
        }

        //harry starts at (0, 0) in my 0 index notation
        mgrid[0][0] = mgrid[rows][cols] = 0;

        //GOAL: find maximum "strength" path but tracking HP lowest
        int lowestStrength = INF; //lowest HP Harry Potter hit, minimum strength is the one that covers that

        //first column
        for(int r = 1; r < rows; r++){
            mgrid[r][0] += mgrid[r-1][0];
        }

        //first row
        for(int c = 1; c < cols; c++){
            mgrid[0][c] += mgrid[0][c-1];
        }

        //bottom-up approach
        for(int r = 1; r < rows; r++){
            for(int c = 1; c < cols; c++){
                int maxStrength = max(mgrid[r-1][c], mgrid[r][c-1]);
                lowestStrength = min(lowestStrength, maxStrength);
                mgrid[r][c] += maxStrength;
            }
        }

        if(lowestStrength <= 0) cout << -lowestStrength + 1 << "\n";
        
        else cout << "1" << "\n";

    }

}
