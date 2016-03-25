#include <iostream>

using namespace std;

int main(){
	float age, age2;

	cout<< "what is your age?"<<endl;
	cin>>age;

	age2 = age*365.25*24*60*60;
	cout<<"you are "<<(age2)<<" seconds old"<<endl;

	return 0;
}