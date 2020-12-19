#include <stdio.h>
#include <bits/stdc++.h>
#include <iostream>

using namespace std;
long long fact(int n){
    if (n>=1){

        n=n*fact(n-1);
        return n;
    }
    else if (n==0){
        return 1;

    }
    else{
    	return -1;
    }
    return 0;
}
int main() {
	//code
	int t;
	cin>>t;
	
	while (t>0){
		long long n;
	    cin>>n;
	    n=fact(n);
	    cout<<n<<endl;
	    t--;
	}
	return 0;
}