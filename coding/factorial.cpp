#include <iostream>
using namespace std;
int ans(long n){
    if (n<10){
       return n; 
    }
    else{
        ans(n%10+n/10);        
    }return ans(n);
}
int main() {
	//code
	int t;
	cin>>t;
	while (t>0){
	    long n;
	    cin>>n;
	    cout<<ans(n);
	    t--;
	}
	
	return 0;
}
