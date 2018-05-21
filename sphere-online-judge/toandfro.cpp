//http://www.spoj.com/problems/TOANDFRO/

#include <iostream>
#include <string>

using namespace std;

/*
*   Nao funciona mas a ideia é converter o input numa string ou array 1D e usar basicamente algo como SIZE*LINE+COL para ir ler a letra certa
*   Há claramente um padrao de leitura
*   tty  -> thisistheeasyoneab - this is the easy one
    hho     -> ttyohhieneesiaabss
    ien     -> 2*size - 1  e dps +1 , alternando
    see
    iaa         0 + 2*size -1 
    ssb

*/
string decrypt(string cypher, int size){
    
    string decrypted = "";
    int step = 2*size-1, read = 0, idx = -1;

    while(read < cypher.size()){
        
        idx++;
        decrypted += cypher[idx];
        idx += step;
        decrypted += cypher[idx];

        read += 2;
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