//Include the necessary libraries
#include <iostream>
#include <iomanip>
#include <cstdlib>
#include <ctime>

using namespace std;


void check(int correct[], int guess[], int& correct_spot, int& incorrect_spot){
	//Check if the i spot in the correct array is in the guess array, if so they got the right spot
	for(int i = 0; i < 4; i++){
		if(correct[i] == guess[i]){
			//Increase the correct spot count
			correct_spot++;
		}

		//If it wasn't there then check for it elsewhere in the guess array, is so they got one in the incorrect spot
		else{
			for(int k = 0; k < 4; k++){
				if(correct[i] == guess[k]){
					//Increase the incorrect spot count
					incorrect_spot++;
				}
			}
		}
	}
}


int main(){
	//Define the array for the correct combination and their guess
	//Define integers for correct spot, incorrect spot and sum
	//Define the difficulty parameters
	int correct[4], guess[4], correct_spot = 0, incorrect_spot = 0, sum = 0;
	int difficulty, randmax, guesses;
	srand(time(0));

	//Ask the user for a difficulty level they would like
	cout<<"Enter a difficulty level 1, 2 or 3:  ";
	cin>>difficulty;

	//Set the max number of guesses and range of numbers based on their choice
	if(difficulty == 1){randmax = 4; guesses = 20;}
	else if(difficulty == 2){randmax = 7; guesses = 15;}
	else{randmax = 10; guesses = 10;}

	//Fill the correct array with random numbers
	//Range is determined based on the difficulty level set above
	for(int i = 0; i < 4; i++){
		correct[i] = (rand()%randmax);
		sum += correct[i];
	}


	//Tell the user how many guesses they have, what the range is, and the sum of their numbers
	cout << "You have " << guesses << " guesses.  Each number is between 0 and " << randmax << "." <<endl;
	cout << "The sum of the numbers is " << sum << endl;
	cout << "Please enter your four numbers seperated by spaces" << endl << endl;

	//Loop through the guessing for the number of guesses they are allowed
	for(int k = 1; k <= guesses; k++){
		//Redefine correct and incorrect spot as 0 each guess
		correct_spot = 0;
		incorrect_spot = 0;

		//Output which guess number they are on and store their input in the guess array
		cout << "Guess " << k << ".   ";
		for(int j = 0; j < 4; j++){
			cin >> guess[j];
		}

		//Run through the check function
		check(correct, guess, correct_spot, incorrect_spot);

		//Output how many they got in the correct spot and how many in the incorrect spot
		cout << "        Right Numbers:   Right location - " << correct_spot << "  Wrong Location - " << incorrect_spot << endl;
	
		//If they got all four in the correct spot then they got the code and they cracked it, end the game
		if(correct_spot == 4){
			cout<<"You cracked it!"<<endl;
			return 0;
		}
	}

	//If they run out of guesses let them know and quit the game
	cout << "You ran out of guesses, better louck next time" << endl;
	return 0;
}