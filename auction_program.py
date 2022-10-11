from art import logo2

print(logo2)
max_bid=0
choice_not_false=True
while choice_not_false:
    bidder_name=input("What is your name?: ")
    bid=int(input("What's your bid?: $"))
    if max_bid<=bid:
        max_bid=bid
        rich_bidder=bidder_name
    choice=input("Are ther any other bidders? Type 'yes' or 'no': ")
    if choice.lower() == 'no':
        choice_not_false=False

print(f"The winner is {rich_bidder} with a bid of {max_bid}" )

#using dictionary
max_bid=0
choice_not_false=True
auction_participants={}
while choice_not_false:
    bidder=input("What is your name?: ")
    bid=int(input("What's your bid?: $"))
    auction_participants[bidder]=bid
    choice=input("Are ther any other bidders? Type 'yes' or 'no': ")
    if choice.lower() == 'no':
        choice_not_false=False

for bidder in auction_participants:
    if auction_participants[bidder]>max_bid:
        max_bid=auction_participants[bidder]
        winner=bidder
print(f"The winner is {winner} with a bid of {max_bid}" )   