from art import logo


auction_list = {}
state = True
while state:
    print(logo)

    name = input("What is your name ?\n")
    bid = int(input("How much would you like to bid?\n$"))
    auction_list[name] = bid

    more_players = input("If there are more players who wish to make a bid type 'yes', else type 'no'.\n").lower()
    if more_players == "no":
        state = False
    print("\n"*100)

print(logo)
highest_bidder = max(auction_list,key=auction_list.get)
print(f"The highest bidder is {highest_bidder} with a total bid of ${auction_list[highest_bidder]}.")
