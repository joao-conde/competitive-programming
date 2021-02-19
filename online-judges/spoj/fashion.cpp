//https://www.spoj.com/problems/FASHION/

#include <bits/stdc++.h>
using namespace std;

int main() {
    
    ios::sync_with_stdio(0); 
    cin.tie();

    int test_cases, participants, score, sum_of_bonds;
    cin >> test_cases;

    while(test_cases--){

        cin >> participants;
        sum_of_bonds = 0;
        vector<int> men, wmen;

        for(int i = 0; i < participants; i++){
            cin >> score;
            men.push_back(score);
        }

        for(int j = 0; j < participants; j++){
            cin >> score;
            wmen.push_back(score);
        }

        sort(men.begin(), men.end());
        sort(wmen.begin(), wmen.end());

        for(int k = 0; k < participants; k++){
            sum_of_bonds += (men.at(k) * wmen.at(k));
        }

        cout << sum_of_bonds << "\n";
    }
}
