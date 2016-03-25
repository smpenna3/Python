#include <cstdlib>
#include <ctime>
#include <cmath>
#include <iostream>

using namespace std;

int main(){
	srand(time(0));
	int roll, height;
	float volume;

	roll = rand()%6+1;
	cout<<"What is the height? ";
	cin>>height;

	volume = float(pow(roll, 2)*height)*(.3333)*3.14159;

	cout<<"The cone is "<<volume<<"."<<endl;

	return 0;
}