//http://www.spoj.com/problems/ADDREV/

#include <cstdio>
#include <cstdlib>

#define MAX_DIGITS 256

using namespace std;


int reverse(int number){
    char str[MAX_DIGITS];
    
    int ndigits = sprintf(str, "%d", number);

    char reversed_str[ndigits];
    reversed_str[ndigits] = '\0';
    for(int i = 0; i < ndigits; i++)
        reversed_str[ndigits-i-1] = str[i];
        
    return atoi(reversed_str);
}

int main(){

    int test_cases;
    scanf("%d", &test_cases);

    for(int i = 0; i < test_cases; i++){
        int a, b, c;
        scanf("%d", &a);
        scanf("%d", &b);

        c = reverse(a) + reverse(b);

        printf("%d\n", reverse(c));
    }
    
    return 0;
}