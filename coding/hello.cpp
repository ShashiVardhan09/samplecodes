#include<iostream>
#include<cmath>
using namespace std;
void add(){
	int a=b+c;
	cout<<a;

}
int main(){
	int a=10;
	int b=20;
	int c=a+b;
	int d=pow(2,5);
	int e=round(-4);
	cout<<"enter age:\n";
	int f;
	string name;
	getline(cin,name);
	//cin>>f;
	cout<<"your age "<<name;
	add();
	return 0;
}