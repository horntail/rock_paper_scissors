from enum import IntEnum
from random import randint

start_int:int = 1
end_int:int = 4

# since we have computer also as a user 
class UserType(IntEnum):
    computer_user = 0
    human_user = 1

class ScoreBoard:
    user_1_score = 0
    user_2_score = 0;
    def update_scores(self, s1, s2):
        self.user_1_score += s1
        self.user_2_score += s2
    def print_scores(self):
        print(f"User 1 score : {self.user_1_score}")
        print(f"User 2 score : {self.user_2_score}")

# the choices or actions available for rock paper scissor game as enum 
class RPSChoices(IntEnum):
    rock, paper, scissors = range(start_int, end_int) 

# get the action from the user as input
def get_user_action():
    all_options = [f"{rps_choice.name}:{rps_choice.value}" for rps_choice in RPSChoices]       
    all_options_str = ",".join(all_options)
    print(f"Choose an action amongst these {all_options_str} now" )
    selected_choice = int(input())
    try:
        return(RPSChoices(selected_choice))
    except Exception as e:
        print(e.__class__)
        print("Invalid input entered, please selected from available choice only")

def get_computer_choice():
    return RPSChoices(randint(start_int, end_int-1))

# the user type and name stored here 
class User():
    name:str
    typeUser:IntEnum

    def __init__(self, name:str, typeUser:int):
        self.name = name
        self.typeUser = UserType(typeUser)
    def printDetails(self):
        print(f"Generated User with Name {self.name} and Type {self.typeUser.name} ")
    def get_user_action(self):
        if(self.typeUser == UserType.human_user):
            action = get_computer_choice()
        else:
            action = get_user_action()
        print(f"{self.name} choose {action.name}" )
        return action

class GameStateToSave:
    user_1:User
    user_2:User
    score_board:ScoreBoard
    def __init__(self, user1:User, user_2:User, score_board:ScoreBoard):
        self.user_1 = user_1
        self.user_2 = user_2
        self.score_board = score_board
    
    # if the user clicks on save the game, this object can be serialised
    #  into json on a file permanenet storage 


# function to compare any two actions selected by user, 
# user names are only passed to print right message 
# returns the scores each user gets after winning or losing 
# tie means both user get 0, 0 score in this trial
def compare_two_actions(choice_1:RPSChoices, choice_2:RPSChoices, user_1:User, user_2:User):
    if(choice_1==choice_2):
        print(f"It is a tie between users {user_1.name} and {user_2.name}")
        return [0, 0]
    elif choice_2 == wins_key_beats_values[choice_1]:
        print(f"User {user_1.name} wins over {user_2.name}")
        return [1, 0]
    else:
        print(f"User {user_2.name} wins over {user_1.name}")
        return [0, 1]

# this represent the pairs or rules of the game
# the key beats the value 
# if there are more coices we can create an array of values which are beaten by a key
wins_key_beats_values = {
        RPSChoices.rock:RPSChoices.scissors, 
        RPSChoices.paper:RPSChoices.rock, 
        RPSChoices.scissors:RPSChoices.paper
    }

def main():
    

    # the main function execution starts here 
    # get user details, this is a 2 player game only
    # both players playing on same screen

    print("Enter user 1 details, User 1 Name, it will be a human by default")
    user_1 = User(input(), UserType.human_user.value)
    user_1.printDetails()

    # only one user can be computer 
    print("Enter Name of second user if human OR enter C?")
    u2_name = str(input())
    computer_name = "c"
    if( u2_name.split(" ")  == computer_name.split(" ")):
        user_2 = User("Computer", UserType.computer_user.value)
    else:
        user_2 = User(u2_name, UserType.human_user)
    user_2.printDetails()


    # fix number of trials at start 
    print("Enter number of trials you want to play")

    # play the game for the number of trials 
    numtrials = int(input())
    score_board = ScoreBoard()
    for i in range(0, numtrials):
        print(f"Running trial number {i}")
        try:
            user_action_1 = user_1.get_user_action()
            user_action_2 = user_2.get_user_action()
            [score_1, score_2] = compare_two_actions(user_action_1, user_action_2, user_1=user_1, user_2=user_2)
            score_board.update_scores(score_1, score_2)
        except Exception as e:
            print("Exception has occured")
        finally:
            continue

    # print final score board
    score_board.print_scores()

if __name__ == "__main__":
    main()

