//Seth Penna, Hertz GE 1110

//Include the necessary libraries and namespaces
#include <iostream>

using namespace std;

int main(){
	//ask the user for the 6 digit serial code
	int serial[6];
	cout<<"Enter the 6 digits of the serial code, with spaces inbetween"<<endl;
	//store the code in an array for easy access
	for(int i = 0; i < 6; i++){
		cin>>serial[i];
	}

	//Step 1
	//check to see if the first value is even or odd by
	//dividing by two and taking the remainder
	//The program will either print Red or Blue depending on even/odd
	if((serial[0] % 2) == 0){
		cout<<"Cut the RED wire"<<endl;}
	else{
		cout<<"Cut the BLUE wire"<<endl;}


	//Step 2
	//Check to see if the second value is greater than the third
	//if it is then print to wait the second value amount of time
	if(serial[1]>serial[2]){
		cout<<"Wait "<<serial[1]<<" seconds before moving on"<<endl;
	}
	//If not, check to see if the second value is divisible by 5
	//and print either the second value plus the fourth,
	//or the second plus the third
	else{
		if((serial[1]%5) == 0){
			cout<<"Wait "<<serial[1]+serial[3]<<" seconds before moving on"<<endl;}
		else{
			cout<<"Wait "<<serial[1]+serial[2]<<" seconds before moving on"<<endl;}
	}


	//Step 3
	//Check if the third value is less than thirty four
	//if it is then cut the Green wire
	if(serial[2]<34){
		cout<<"Cut the GREEN wire"<<endl;}
	//Check if the third value is between 34 and 66
	//if it is then cut the Yellow wire
	else if(serial[2] <= 66 and serial[2] >= 34){
		cout<<"Cut the YELLOW wire"<<endl;}
	//The only remaining possibility is over 66
	//if it is then cut the Orange wire
	else{
		cout<<"Cut the ORANGE wire"<<endl;}


	//Step 4
	//Check if the sixth value is greater than the first,
	//and also that the sixth value is greater than
	//the third.
	//If it is, cut the white wire
	if(serial[5]>serial[0] and serial[5]>serial[2]){
		cout<<"Cut the WHITE wire"<<endl;}
	//If it isn't, cut the Black wire.
	else{
		cout<<"Cut the BLACK wire"<<endl;}


	//Step 5
	//Check if the fifth plus sixth value are greater than or equal to 
	//the second plus the fourth value; or if the fourth is greater
	//than or equal to 100.
	//If it is then cut the Silver wire
	if(((serial[4]+serial[5]) >= (serial[1]+serial[3])) or serial[3] >= 100){
		cout<<"Cut the SILVER wire"<<endl;}
	//If the above is not true then cut the Copper wire
	else{
		cout<<"Cut the COPPER wire"<<endl;}


	return 0;
}