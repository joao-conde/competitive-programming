//https://www.spoj.com/problems/ANARC09A/

#include <bits/stdc++.h>
using namespace std;


int requiredOperations(string line){

    int ops = 0, maxOpen = line.size() / 2;
    stack<char> open;

    for(int i = 0; i < line.size(); i++){

        if(line[i] == '{'){

            if(maxOpen == 0){
                ops++;
                open.pop();
            }
            else{
                open.push('{');
                maxOpen--;
            }

        }
        else{

            if(open.empty() && maxOpen > 0){
                open.push('{');
                maxOpen--;
                ops++;
            }
            else
                open.pop();
        }
    }

    return ops;
}


int main(){

    ios::sync_with_stdio(0);
    cin.tie();

    int testNo = 1;
    string line;
    while(true){

        getline(cin, line);

        if(line[0] == '-') break;

        cout << testNo << ". " << requiredOperations(line) << endl;
        testNo++;
    }
}
