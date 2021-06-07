import random
card_list = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def random_card_generator():
    cards = []
    first_card = random.choice(card_list)
    second_card = random.choice(card_list)
    cards.extend([first_card, second_card])
    return cards

def one_card_adder(card_list):
    random_card = random.choice(card_list)
    card_list.append(random_card)


def result_calculator(my_cards, computer_cards):
    my_cards_sum = sum(my_cards)
    computer_cards_sum = sum(computer_cards)
    computer_margin = 21 - computer_cards_sum
    my_cards_margin = 21 - my_cards_sum

    if my_cards_sum > 21:
        print("You went over. You lose 😤")
    elif computer_cards_sum > 21:
        print("Opponent went over. You win 😁 ")
    elif my_cards_sum == computer_cards_sum:
        print("Match Draw.")
    elif computer_margin > my_cards_margin:
        print("You Win")
    else:
        print("Computer Wins")


def main():
    get_card = 'y'
    my_cards = random_card_generator()
    computer_cards = random_card_generator()
    print(f"Your cards: {my_cards}. Final Score: {sum(my_cards)}")


    print(f"Computer's first card: {computer_cards[0]}")
    get_card = input(f"Type 'y' to get another card, type 'n' to pass: ")
    while get_card == 'y':
        one_card_adder(my_cards)
        print(f"Your cards: {my_cards}. Final Score: {sum(my_cards)}")
        while sum(computer_cards) <= 17:
            one_card_adder(computer_cards)
        if sum(my_cards) <= 21:
            get_card = input(f"Type 'y' to get another card, type 'n' to pass: ")



    print(f"Your final hand: {my_cards}. Final Score: {sum(my_cards)}")
    print(f"Computer's final hand: {computer_cards}. Final Score: {sum(computer_cards)}")
    result_calculator(my_cards, computer_cards)
    


main()