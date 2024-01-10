'''
game logic:
1. create an array, rock, paper, scissor
2. select a random option out of this
3. store as computer's choice
4. ask user to input choice
5. store this as user's choice
6. if user's choice == computer's choice
    7. display try again
    8. repeat from step 2
9. else, check which combination it is
    U       C           S_U         S_C
    rock    paper       0           +1
    paper   scissor     0           +1
    scissor rock        0           +1
    rock    scissor     +1           0
    paper   rock        +1           0
    scissor paper       +1           0        
10. ask if the user wants another turn
    11. if yes, repeat from step 2
    12. if no, display final scores
'''

import random
actions = ['rock', 'paper', 'scissors']
users_score = 0
computers_score = 0
winner = ""

def make_selection(actions):
    computers_choice = random.choice(actions)
    return computers_choice

def catching_errors():
    return "try again"

def main(users_score, computers_score, winner):
    
    users_choice = input("Choose one: rock, paper, scissors: \t")
    computers_choice = make_selection(actions)

    if computers_choice != users_choice:
        combination = users_choice + computers_choice

        match combination:

            case "rockpaper":
                computers_score += 1
                winner = "Computer"
            case "paperscissors":
                computers_score += 1
                winner = "Computer"
            case "scissorsrock":
                computers_score += 1
                winner = "Computer"

            case "rockscissors":
                users_score += 1
                winner = "User"
            case "paperrock":
                users_score +=1
                winner = "User"
            case "scissorspaper":
                users_score +=1
                winner = "User"
            case _:
                print(catching_errors)
                make_selection(actions)
            
    else:
        print(catching_errors())
        make_selection(actions)

    return ("Computer chose {comp} .The winner is "+ winner+"!").format(comp = computers_choice)

print(main(0,0, ""))