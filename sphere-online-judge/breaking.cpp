//http://www.spoj.com/problems/BREAKING/

#include <iostream>
#include <vector>

using namespace std;



/*
*   Wrong solution: 
*   how to get a list of primes up to N
*   check if they divide N correctly
*/
vector<int> get_prime_divisors(int dividend){
    vector<int> primes;

    int prime = 2;
    while(true){

        if(dividend % prime == 0){
            primes.push_back(prime);
            dividend /= prime;
            cout << prime << " divides " << dividend;
        }

        if(dividend == 1)
            return primes;

        prime++;
    }

    return primes;
} 


void print_primes(vector<int> primes){
    for(int i = 0; i < primes.size(); i++)
        cout << primes.at(i) << endl;
}



int main(){

    int test_cases, n;
    cin >> test_cases; cin.ignore();
    
    for(int i = 0; i < test_cases; i++){
        cin >> n; cin.ignore();

        cout << "Case " << i+1 << ": "; 
        print_primes(get_prime_divisors(n));
    }

    return 0;
}