//http://www.spoj.com/problems/BREAKING/

#include <math.h>

#include <iostream>
#include <vector>

using namespace std;

//TODO: solve this, getting WA

//Eratosthenes' Sieve
vector<int> generate_primes_upto(int n){
    vector<int> primes_upto_n; 
    
    int sqrt_n = sqrt(n);
    int not_prime[sqrt_n] = {}; //all inititated as '0' = prime, '1' = not prime

    for(int i = 2; i < sqrt_n; i++){

        if(not_prime[i] == 1) continue;

        primes_upto_n.push_back(i);
        for(int j = i; j < sqrt_n; j+=i){
            not_prime[j] = 1;
        }

    }
    
    return primes_upto_n;
}


//global variable => heap
vector<int> primes;

int main(){

    int test_cases, n;
    cin >> test_cases; 
    
    primes = generate_primes_upto(1000000);

    
    for(int i = 0; i < test_cases; i++){
        cin >> n;

        cout << "Case " << i+1 << ":";

        for(int factor: primes){
            if(n % factor == 0){
                cout << " ";
                cout << factor;
            }
        }

        cout << endl;           
    }

    return 0;
}