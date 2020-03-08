#include <bits/stdc++.h>
using namespace std;

struct BinaryTree{
    char root;
    BinaryTree *left, *right;
};

void build_tree(string infix, string prefix){

    char root = prefix[0];
    cout << root << endl;
    int left_size = infix.rfind(root);
    
    BinaryTree *left, *right;
    if(left_size > 0){
        build_tree(infix.substr(0, left_size), prefix.substr(1, left_size));
    }

    if(infix.size() - left_size - 1 > 0){
        build_tree(infix.substr(left_size+1), prefix.substr(left_size+1));
    }

}

void print_binary_tree(BinaryTree *tree){
    cout << tree->root << endl;
    if(tree->left != nullptr)   print_binary_tree(tree->left);
    if(tree->right != nullptr)   print_binary_tree(tree->right);
}

int main() {
    ios::sync_with_stdio(0); 
    cin.tie();
    
    string infix, prefix;
    while(getline(cin, infix)){
        getline(cin, prefix);
        cout << "TREE\n";
        build_tree(infix, prefix);

        //print_binary_tree(tree);

    }

}