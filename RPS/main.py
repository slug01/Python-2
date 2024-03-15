# importing essential libraries
import random 


#creating a class named rock_paper_seasor
class rock_paper_scissors: 
    # initializing the instance variable in list.
    def __init__(self):
        self.choices = ['rock','paper','scissors']

    # this method is responsible for getting the computer choice from the choices list using random
    def get_computer_choice(self):
        return random.choice(self.choices)
    
    # this block determine the winner of the game..
    def determine_winner(self, user_choice, computer_choice):

        # comparing user choice and the computer choice...using if else statement.
        if user_choice == computer_choice:
            return "Its a Tie."
        elif (user_choice == 'rock' and computer_choice == 'scissors') or (user_choice =='paper' and computer_choice == 'rock') or (user_choice == 'scissors' and computer_choice == 'paper'):
            return "You win."
        else:
            return "Computer Win"

    # this method is the main part of the game where user input is taken and loop is used to play again or not.
    def play_game(self):
        print("Lets play Rock, Paper, Scissors.")
        while True:
            
            # taking input for the user's choice
            user_choice = input("Enter your Choice(rock,paper,scissors):")
            print("Your choice is ",user_choice)
            if user_choice not in self.choices:
                print("Your choice is not in list.")
                continue
            computer_choice = self.get_computer_choice()
            print(f"You Choose {user_choice}, computer choose {computer_choice}")
            print(self.determine_winner(user_choice, computer_choice))
            play_again = input("Do you want to play again (Yes/No)").lower

            if play_again != "yes":
                print("Thanks for playing.")

                break

            

# This line creates an instance of the class, representing the game object.
game = rock_paper_scissors()

# This line calls the `play_game()` method on the `game` object to start playing the game.
game.play_game()
