from art import logo
import os

others = True
bidding_dict = {}

os.system('clear')
print(logo)

def highest_counter():
    max = 0
    max_key = "" 
    for key in bidding_dict:
        if max < bidding_dict[key]:
            max = bidding_dict[key]
            max_key = key
    return max_key

while others:
    name = input("Enter your name : ")
    bid = int(input("Enter your bid : "))

    bidding_dict[name] = bid

    users_left = input("Are there other users left to bid? If not enter NO : ").lower()

    if users_left == "no":
        others = False
    else:
        os.system('clear')
        print(logo)

for keys in bidding_dict:
    if keys == highest_counter():
        print(f"The winner is {keys} with the highest bid of {bidding_dict[keys]}")

