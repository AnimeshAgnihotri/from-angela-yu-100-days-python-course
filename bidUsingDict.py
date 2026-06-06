print("online bid\n")
 
def max_bid(bids):
    max_value = 0
    winner = ""
    for bidder in bids:
        if bids[bidder] > max_value:
            max_value = bids[bidder]
            winner = bidder
    print(f"Winner is {winner} with bid {max_value}")
 
bids = {}
answer = True
 
while answer:
    a = input("do you want to enter for bid y or n: ").lower()
   
    if a == 'y':
        name = input("enter your name: ")
        name=name.title()
        bid = int(input("enter your bid: "))
        bids[name] = bid
    else:
        answer = False
 
print(bids)
max_bid(bids)
 
