import replit
import art

print(art.logo)
print("Welcome to the secret auction program")

bidders = {}
   
def highest_bid(dict):
    bid_high = 0
    for bidder in bidders:
        bid_amount = bidders[bidder]
        if bid_amount > bid_high:
            bid_high = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${bid_high} ")        


any_bidder_to_add = True    
while any_bidder_to_add :  
    name = input("What is your name? : ")
    price = int(input("what is your bid? : $"))
    bidders[name] = price
    
    any_bidder_to_add = input("are there any other bidders? Type 'yes' or  'no': ").lower()
    replit.clear()

    if  any_bidder_to_add == 'no':
        any_bidder_to_add = False

highest_bid(bidders) 
