//https://www.spoj.com/problems/ANARC05B/

#include <bits/stdc++.h>
using namespace std;

int main() {
    
    ios::sync_with_stdio(0); 
    cin.tie();

    while(true){

        int length1, length2;
        cin >> length1;
        if(length1 == 0) 
            break;         

        vector<int> seq1(length1);
        for(int i = 0; i < length1; i++) cin >> seq1[i];
        
        cin >> length2;
        vector<int> seq2(length2);
        for(int i = 0; i < length2; i++) cin >> seq2[i];
        
        //following solution takes advantage of both being ordered
        int idx1 = 0, idx2 = 0; 
        long long segmentSum1 = 0, segmentSum2 = 0;
        while(idx1 < length1 || idx2 < length2){

            //intersection
            if(idx1 < length1 && idx2 < length2 && seq1[idx1] == seq2[idx2]){
                segmentSum1 += seq1[idx1];
                segmentSum2 += seq2[idx2];
                segmentSum1 = segmentSum2 = max(segmentSum1, segmentSum2);
                idx1++; idx2++;
            }
            else if(idx1 >= length1){ //no more seq1 elements
                segmentSum2 += seq2[idx2];
                idx2++;
            }
            else if(idx2 >= length2){ //no more seq2 elements
                segmentSum1 += seq1[idx1];
                idx1++;
            }
            else if(seq1[idx1] < seq2[idx2]){ //first element lower than second
                segmentSum1 += seq1[idx1];
                idx1++;
            }
            else if(seq1[idx1] > seq2[idx2]){ //first element bigger than second
                segmentSum2 += seq2[idx2];
                idx2++;
            }
            
        }

        cout << max(segmentSum1, segmentSum2) << "\n";

    }

}
