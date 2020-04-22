#Use alpha vantage
Stock = topstocks.py()
#get the 5 best stocks and put it in Stock[]

purse = 1000 #1000 dollars fake to try the code

price = []
for Stock in Stock:
    price += getprice(Stock)
# get the prices of all the stocks
    for i in range(5):
        if price >= High:
            Stock = High
            Buyaction(purse)

        if price <= Low:
            Newprice = Low
            Sellaction(purse)
