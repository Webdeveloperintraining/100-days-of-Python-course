import art

print(art.logo)

print("Welcome to the secret auction program.")

auction_status = []

def insert_bidder(name,bid):
    auction_status.append({"name":name, "bid":bid,})
    
def determine_winner():
    highest_bidder = ''
    highest_bid = 0 
    for bidder in auction_status:
        if highest_bid < bidder["bid"]:
            highest_bid = bidder["bid"]
            highest_bidder = bidder["name"]
    print(f'The winner is {highest_bidder}, with a bid of ${highest_bid}')

more_bidders  = True
while more_bidders:
    name = input ("What is your name?: ")
    bid = int(input("What's your bid? "))
    insert_bidder(name,bid)
    bidders = input("Are there any other bidders? (Type 'yes' or 'no') ")
    if bidders.lower() != 'yes':
        more_bidders  = False

determine_winner()