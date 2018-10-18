//https://www.spoj.com/problems/TWENDS/

#include <bits/stdc++.h>
using namespace std;


int cards[1005], memo[1005][1005];

int computeSmartMaxPts(int lidx, int ridx){

    if(lidx > ridx) return 0;

    if(memo[lidx][ridx] != -1) return memo[lidx][ridx];
    
    /*
        Option 1:
            - choose first card in range (left)
            - greedy now chooses the max value card off of the 2 ends

            opt1 = cards[i] + func(i + 1, j - 1) or opt1 = cards[i] + func(i + 2, j)
            since you take card[i] (leftmost card) and can either have a state where greedy takes from right (so j-1 and your i+1) or also takes from 
            left (so i + 2)

        Option 2:
            - choose last card in range (right)
            - greedy now chooses the max value card

            opt2 = cards[j] + func(i + 1, j - 1) or cards[j] + func(i, j - 2) similiar to previous option
    */

    int opt1, opt2;

    //assume we pick first card -> cards[i]
    //remains cards(i+1 to j), which end has higher value for the greedy?
    
    //left end has higher value
    if(cards[lidx+1] >= cards[ridx]){
        opt1 = cards[lidx] + computeSmartMaxPts(lidx + 2, ridx);
    }
    else{ //right end has higher value
        opt1 = cards[lidx] + computeSmartMaxPts(lidx + 1, ridx-1);
    }

    //assume we pick last card -> cards[j]
    //left end has higher value
    if(cards[lidx] >= cards[ridx-1]){
        opt2 = cards[ridx] + computeSmartMaxPts(lidx + 1, ridx - 1);
    }
    else{ //right end has higher value
        opt2 = cards[ridx] + computeSmartMaxPts(lidx, ridx - 2);
    }

    return memo[lidx][ridx] = max(opt1, opt2);
}

int main(){
    
    ios::sync_with_stdio(0); 
    cin.tie();


    int n, game = 1;
    while(cin >> n){

        if(n == 0) break;

        memset(memo, -1, sizeof(memo));

        int total = 0;
        for(int i = 0; i < n; i++){
            int pts; cin >> pts;
            total += pts;
            cards[i] = pts;
        }

        //from total = smart + greedy and smart - greedy = diff
        //diff = 2 * smart - total
        cout << "In game " << game << ", the greedy strategy might lose by as many as " << abs(2 * computeSmartMaxPts(0, n-1) - total) << " points.\n";
        game++;
    }

}
