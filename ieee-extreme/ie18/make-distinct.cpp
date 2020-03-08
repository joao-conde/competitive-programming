#include <bits/stdc++.h>

#define MAX 3000000

using namespace std;

int num[MAX];

int main(){
    
    int n, ops = 0; cin >> n;
    while(n--){
        int el; cin >> el;
        if(num[el] == 0){
            num[el] = 1;
            continue;
        }
        else{
            int offset = 1;
            while(true){
                ops++;
                if(num[el + offset] == 0){
                    num[el + offset] = 1;
                    break;
                }
                else if(num[el - offset] == 0){
                    num[el - offset] = 1;
                    break;
                }
                offset++;
            }
        }
    }

    cout << ops << endl;
}