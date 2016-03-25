//Include necessary libraries
#include <iostream>
#include <iomanip>
#include <cstdlib>
#include <ctime>

using namespace std;


void check(int correct[], int guess[], int& correct_spot, int& incorrect_spot){
	for(int i = 0; i < 4; i++){
		if(correct[i] == guess[i]){
			correct_spot++;
		}
		else{
			for(int k = 0; k < 4; k++){
				if(correct[i] == guess[k]){
					incorrect_spot++;
				}
			}
		}
	}
}


int main(){
	//Define the arrays to store the guesses and correct answers
	//Define the integers to store correct and incorrect spot, as well as sum
	int correct[4], guess[4], correct_spot = 0, incorrect_spot = 0, sum = 0;
	srand(time(0));

	//Fill the correct array with 4 random digits
	for(int i = 0; i < 4; i++){
		correct[i] = (rand()%10);
		sum += correct[i];
	}

	cout << "The sum of the numbers is " << sum << endl;
	cout << "Please enter your four numbers seperated by spaces" << endl << endl;

	for(int k = 1; k <= 12; k++){
		correct_spot = 0;
		incorrect_spot = 0;

		cout << "Guess " << k << ".   ";
		for(int j = 0; j < 4; j++){
			cin >> guess[j];
		}

		check(correct, guess, correct_spot, incorrect_spot);

		cout << "        Right Numbers:   Right location - " << correct_spot << "  Wrong Location - " << incorrect_spot << endl;
	
		if(correct_spot == 4){
			cout<<"You cracked it!"<<endl;
			return 0;
		}
	}

	return 0;
}