#include <iostream>

using namespace std;

int main(){
	float grade[10];
	float average, sum = 0;

	for(int i=0; i<10; i++){
		cout<<"Enter the grade: ";
		cin>>grade[i];
	}

	for(int k=0; k<10; k++){
		sum += grade[k];
	}

	average = sum/10;

	cout<<"The average is "<<average<<endl;

	return 0;
}