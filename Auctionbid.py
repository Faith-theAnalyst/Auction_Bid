import os
print("Welcome to the Auction ")
another_bid = "Yes"
bids = {}
while another_bid == "yes":
    bidder_name = input("Enter your name: ")
    bid_price = float(input("Enter bid amount: "))
    bids[bidder_name] = bid_price
    another_bid = ("Are there other users who want to bid? yes or no: ").lower()
    if another_bid == "yes":
        os.system("cls")
max_value = max(bids.values())
max_bidder_list = [key for key,value in bids.items() if value == max_value]
max_bidder = "".join(max_bidder_list)
print(f"Thanks for all the bids. The winner of this bid round is {max_bidder} ")

