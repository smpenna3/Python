//Seth Penna GE 1110 Hertz

//Include the necessary libraries
#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

int main(){
	//Define a variable for the current and new diseased decimal
	double diseased_current = 0.0001;
	double diseased_new;
	double r;

	//Ask the user for an R value so that it can be changed with each run
	cout<<"Input the infection rate value ";
	cin>>r;

	//Run a loop increasing the week each time
	for(int week = 1; week <= 52; week++){
		//If the diseased percentage is over 50% quit the program
		if(diseased_current >= 0.5){
			return 0;
		}

		//If the diseased percentage is under 50%,
		//print the diseased level
		cout<<setprecision(3)<<"week "<<week<<"  "<<diseased_current*100<<" percent diseased"<<endl;
		
		//And also calculate the new diseased percentage based
		//on the R value
		diseased_new = diseased_current * r * (1-diseased_current);
		
		///Finally, set the current diseased level to that which was calculated
		diseased_current = diseased_new;
	}


	return 0;
}