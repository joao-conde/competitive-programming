//https://www.spoj.com/problems/ANARC05B/

#include <bits/stdc++.h>
using namespace std;

/* TIL:
*   1 - ...
*   2 - ...
*   3 - ...
*/

#define MAX_SOLUTION 10000000
#define MAX_ELEMENTS 10000

int dp[MAX_ELEMENTS][MAX_ELEMENTS];

bool isSolution(int val){




    return false;
}

int main() {
    
    ios::sync_with_stdio(0); 
    cin.tie();

    while(true){

        int length1, length2; 
        cin >> length1;
        
        if(length1 == 0) 
            break;
        else
            cin >> length2;

        for(int i = 0; i < length1; i++) cin >> dp[0][i];
        for(int i = 0; i < length2; i++) cin >> dp[i][0];

        int lb = 0, ub = MAX_SOLUTION, mid;
        while(ub >= lb){

            cout << "TESTING: " << mid << endl;
            mid = (lb + ub) / 2;

            if(isSolution(mid){
                mid = ub - 1;
            }
            else{
                mid = lb + 1;
            }

        }


        cout << lb << " - " << mid << " - " << ub << endl;
    }


}
