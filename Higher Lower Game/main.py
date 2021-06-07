import random
from os import system, name
from game_data import data
from logo import logo, vs

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def check_input(first_player, second_player, user_input):
    first_followers = first_player['follower_count']
    second_followers = second_player['follower_count']

    if first_followers > second_followers and user_input == 'A':
        return first_player
    elif first_followers > second_followers and user_input == 'B':
        return False
    elif second_followers > first_followers and user_input == 'A':
        return False
    elif second_followers > first_followers and user_input == 'B':
        return second_player


def main():
    first_player = random.choice(data)
    second_player = random.choice(data)
    check_user_input = True
    user_score = 0

    while check_user_input != False:
        clear()
        print(logo)
        print(f"Compare A: {first_player['name']}, a {first_player['description']} from {first_player['country']}")
        print(vs)
        print(f"Against B: {second_player['name']}, a {second_player['description']} from {second_player['country']}")
        user_input = input("Who has more followers? Type 'A' or 'B': ")
        
        check_user_input = check_input(first_player, second_player, user_input)

        if check_user_input == second_player:
            first_player = second_player
            second_player = random.choice(data)
            user_score += 1
            print(f"You're right. Current Score: {user_score}")
        elif check_user_input == first_player:
            second_player = random.choice(data)
            user_score += 1
            print(f"You're right. Current Score: {user_score}")
        else:
            clear()
            print(logo)
            print(f"Sorry that's wrong. Final score: {user_score}")
    
        
    
main()