#include <iostream>

using namespace std;

int main(){

    int t,n;
    char a[200],a2[200];

    cin >> t;
    cin >> n;

    for(int i=0; i<t; i++){
        cin.getline(a,n);

        for(int j=0; j<n-1; j++){
            if(a[j] == a[j+1]){
                a2[j] = '-';
            }
            else{
                a2[j] = '+';
            }
        }
        cout << a2[0]<<endl;
    }


    return 0;
}