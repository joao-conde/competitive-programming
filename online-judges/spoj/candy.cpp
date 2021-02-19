//http://www.spoj.com/problems/CANDY/

#include <bits/stdc++.h> //Includes ALL c++ files needed

using namespace std;

/* TIL:
*   1 - #include <bits/stdc++.h> includes ALL c++ files needed
*/


int main(){

    ios::sync_with_stdio(0); //Input and output become more efficient.
    cin.tie();

    int moves, goal, ncandies, npackets = 0;
    while(true){
        cin >> npackets;

        if(npackets == -1) break;

        //Reading packets candy and computing total
        vector<int> packets(npackets);
        ncandies = 0;
        for(int i = 0; i < npackets; i++){
            cin >> packets[i];
            ncandies += packets[i];
        }

        //No possible equal distribution of candy
        if(ncandies % npackets != 0){
            cout << -1 << endl;
            continue;
        }

        //Desired number of candy per packet
        goal = ncandies/npackets;

        //Compute minimum candy moves required
        moves = 0;
        for(int j = 0; j < npackets; j++){
            //Need to remove N candy from this packet => N moves at least
            if(packets[j] > goal){
                moves += packets[j] - goal;
            }
        }

        cout << moves << endl;
    }

    return 0;
}
