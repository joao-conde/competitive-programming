//https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=3&page=show_problem&problem=38

#include <bits/stdc++.h>
using namespace std;

/*
 *  Builds a bin from input.
 */
vector<int> makeBin(stringstream &ss){

    vector<int> bin(3);
    string dummy;

    for(int i = 0; i < 3; i++){
        ss >> dummy;
        bin[i] = stoi(dummy);
    }

    return bin;
}

/*
 *  Calculates minimum moves with specified bin type.
 *  Minimum amount of moves is the amount of bottles in the bin not from the type specified.
 */
int minMovesBin(vector<int> &bin, char type){

    if(type == 'B') return bin[1] + bin[2];
    if(type == 'G') return bin[0] + bin[2];
    if(type == 'C') return bin[0] + bin[1];

    return -1;
}


/*
 *  Calculates minimum moves for the set of bins with specified configuration.
 */
int minMovesSet(vector<int> &bin1, vector<int> &bin2, vector<int> &bin3, string conf){
    return minMovesBin(bin1, conf[0]) + minMovesBin(bin2, conf[1]) + minMovesBin(bin3, conf[2]); 
}


/*
 *  Computes the optimal configuration for the bin set, minimizing movements made.
 *  If 2 configurations require the same amount of movements, chooses the alphabetically first one.
 */
string computeEcoBinPack(vector<int> &bin1, vector<int> &bin2, vector<int> &bin3){
    
    //alphabetical order 
    string configs[6] = {"BCG", "BGC", "CBG", "CGB", "GBC", "GCB"};
    int moves[6], min;

    for(int i = 0; i < 6; i++){
        moves[i] = minMovesSet(bin1, bin2, bin3, configs[i]);
    }

    min = *min_element(moves, moves + 6);

    //first solution that meets the minimum is the first alphabetically aswell (ordered configs)
    int j;
    for(j = 0; j < 6; j++){
        if(moves[j] == min) break;
    }    

    return configs[j] + " " + to_string(min);
}


int main() {

    ios::sync_with_stdio(0); 
    cin.tie();

    string input;
    while(getline(cin, input)){
        
        stringstream ss(input);
        vector<int> bin1, bin2, bin3;

        bin1 = makeBin(ss);
        bin2 = makeBin(ss);
        bin3 = makeBin(ss);
        
        cout << computeEcoBinPack(bin1, bin2, bin3) << "\n";
    }

}
