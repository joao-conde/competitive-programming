#include <iostream>
#include <vector>

using namespace std;


//-1 output terminates own program? X?D!?

int main(){

    ios::sync_with_stdio(0); //Input and output become more efficient.
    cin.tie();

    int moves, goal, ncandys, npackets = 0;
    while(true){
        cin >> npackets;

        if(npackets == -1) break;

        //Reading packets candy and computing total
        vector<int> packets(npackets);
        ncandys = 0;
        for(int i = 0; i < npackets; i++){
            cin >> packets[i];
            ncandys += packets[i];
        }

        //No possible equal distribution of candy
        if(ncandys % npackets != 0){
            cout << -1 << endl;
            break;
        }

        //Desired number of candy per packet
        goal = ncandys/npackets;
        
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