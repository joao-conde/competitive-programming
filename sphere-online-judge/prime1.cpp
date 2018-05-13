//http://www.spoj.com/problems/PRIME1/

#include <iostream>
#include <cstdio>

#define FOR(i,n)   for (int i = 0 ; i < (n) ; i++)

using namespace std;

int is_prime(unsigned int number) {
    if (number <= 1) return 0; // zero and one are not prime
    
    unsigned int i;
    for (i=2; i*i<=number; i++) { //check untill sqrt(number)
        if (number % i == 0) return 0;
    }

    return 1;
}

int main(){

    int test_cases;

    scanf("%d", &test_cases);

    FOR(i,test_cases){
        int m, n, p;

        scanf("%d", &m);
        scanf("%d", &n);

        p = m;

        while(p <= n){
            if(is_prime(p)) printf("%d\n",p);
            p++;
        }

        printf("\n");
    }

    return 0;
}