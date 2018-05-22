//http://www.spoj.com/problems/TOANDFRO/

#include <iostream>
#include <string>

using namespace std;

/*
*   começa num ponto, le, anda para a direita, le, anda para a esquerda, repete
*   anda o que sobrar para a direita * 2 + 1 e o que sobrar para a esquerda + 1
*   dá duas voltas por assim dizer mais a casa de "descer a coluna"
*/
string read_chypher_col(string cypher, int size, int col){
    string decrypted = "";

    int step_l = col * 2 + 1;
    int step_r = (size - col - 1)*2 + 1;
    int col_length = cypher.size() / size, read = 0, idx = col;

    while(read < col_length){
        decrypted += cypher[idx];

        idx += step_r;
        decrypted += cypher[idx];
        
        idx += step_l;

        read += 2;
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
    
        cout << decrypt(cypher, size);
        
    }

    return 0;
}