# BLIND AUCTION PROGRAM

"""
The objective is to write a program that will collect the names and bids of different people. 
The program should ask for each bidder's name and their bid individually.
"""
import os
# Create a dictionary to store the name and bid of each bidder
bids = {}

print("Welcome to the Blind Auction Program")
print("Please enter your name :" )
name = input()
print("Please enter your bid :")
bid = int(input())
bids[name] = bid

# Function to chech the highest bid
def highest_bid(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")
    

reenter = True
while reenter:
    print("Is there another bidder? (yes/no)")
    reenter = input()
    if reenter == "yes":
        os.system('clear')
        print("Please enter your name :" )
        name = input()
        print("Please enter your bid :")
        bid = int(input())
        bids[name] = bid
    else:
        reenter = False

# Clear the console
os.system('clear')
highest_bid(bids)