//https://www.spoj.com/problems/FASHION/

#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0); 
    cin.tie();

    int test_cases, participants, score;
    cin >> test_cases;

    while(test_cases--){

        cin >> participants;
        vector<int> men(participants), wmen(participants);

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

    }
}
