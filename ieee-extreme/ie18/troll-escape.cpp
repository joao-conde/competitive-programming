#include <bits/stdc++.h>
using namespace std;


int query(string bit_string){

    cout << "Q";

    for(char b: bit_string){
        cout << " " << b; 
    }

    cout << endl;
    cout.flush();

    int troll_answer;
    cin >> troll_answer;
    return troll_answer;
}

int main(){

    srand(time(NULL));
    int t;
    cin >> t;

    while(t--){

        int str_size;
        cin >> str_size;

        string guess = "";
        for(int i = 0; i < str_size; i++){
            guess += to_string(rand() % 2); //0 or 1
        }

        int correct_bits = query(guess);

        vector<int> str_idxs_processed;
        while(str_idxs_processed.size() < str_size){

            if(correct_bits == str_size) break;
            
            int str_idx;
            vector<int>::iterator it;
            do{
                str_idx = rand() % str_size;
                it = find(str_idxs_processed.begin(), str_idxs_processed.end(), str_idx);
            }
            while(it != str_idxs_processed.end());
            
            str_idxs_processed.push_back(str_idx);
            
            string new_guess = guess;
            if(new_guess[str_idx] == '1')
                new_guess[str_idx] = '0';
            else
                new_guess[str_idx] = '1';

            int new_guess_correct = query(new_guess);

            if(new_guess_correct > correct_bits){
                guess = new_guess;
                correct_bits = new_guess_correct;
            }

            str_idx++;
        }

        cout << "A";
        for(char b: guess){
            cout << " " << b; 
        }
        cout << endl;

    }

}