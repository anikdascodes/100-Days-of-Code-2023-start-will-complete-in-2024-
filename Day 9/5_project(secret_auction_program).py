from replit import clear
#HINT: You can call clear() to clear the output in the console.

#Show logo from art.py
from art import logo
print(logo)

bids = {}

bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
    #ask for name input
    name = input("What is your name?\n")
    #ask for bid price
    price = int(input("What is your bid?\n$"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        clear()  # This function is come from replit module to clear the console









