//http://www.spoj.com/problems/TOANDFRO/

#include <iostream>
#include <string>

using namespace std;

/*
*   Reads a "column" of the "matrix".
*   Reads the first "line" element of the "column", moves to the right 2*X + 1, reads that element, moves to the left
*   2*Y+1 and reads that element. Does this cycle untill no more string to process.
*   X = number of "columns" to the right
*   Y = number of "columns" to the left
*/
string read_chypher_col(string cypher, int size, int col){
    string decrypted = "";

    int step_l = col * 2 + 1;
    int step_r = (size - col - 1)*2 + 1;
    int cypher_size = cypher.size(), idx = col;

    while(idx < cypher_size){

        decrypted += cypher[idx];

        idx += step_r;
        if(idx >= cypher_size) break; //no more string

        decrypted += cypher[idx];
        
        idx += step_l;
    }


    return decrypted;
}

string decrypt(string cypher, int size){
    string decrypted = "";
    
    int i = 0;
    while(i < size){
        decrypted += read_chypher_col(cypher, size, i);
        i++;
    }

    return decrypted;
}

int main(){

    int size;
    string cypher = "";

    while(true){
        
        cin >> size;
        if(size == 0)
            break;

        
        cin >> cypher;
    
        cout << decrypt(cypher, size) << endl;
        
    }

    return 0;
}