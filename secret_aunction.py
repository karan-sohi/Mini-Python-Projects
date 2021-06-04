from os import system, name

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def bid_checker(bidders_record):
    highest_bid = 0
    for person in bidders_record:
        if person["bid"] > highest_bid:
            highest_bid = person["bid"]
            name = person["name"]
    print("The winner is", name, 'with a bid of', highest_bid)



def get_user_input():
    bidders_record = []
    other_bidders = 'yes'
    while other_bidders == 'yes':
        person_record = {}
        name = input("What is your name?: ")
        bid = int(input("What's your bid($)?: "))
        other_bidders = input("Are there any other bidders? Type 'yes' or 'no'. \n")
        person_record["name"] = name
        person_record["bid"] = bid
        bidders_record.append(person_record)
        clear()
    return bidders_record

def main():
    bidders_record = get_user_input()
    bid_checker(bidders_record)


main()