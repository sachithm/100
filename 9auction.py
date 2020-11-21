import art
from os import system

logo = art.auction_logo

master_list = {}
keep_going = True

def auction(name, bid):
    master_list[name] = bid

def call_winner():
    working_number = 0

    for entry in master_list:
        if working_number < master_list[entry]:
            working_number = master_list[entry]
            working_winner = entry

    print(logo)
    print(f"{working_winner} has won the auction with a bid of £{working_number}!")

while keep_going == True:
    print(logo)
    input_name = input("What is your name?: ")
    input_bid = int(input("What's your bid?: £"))
    input_others = input("Are there any other bidders? ").lower()

    auction(input_name, input_bid)

    system('clear')

    if input_others == "no":
        keep_going = False
        call_winner()
