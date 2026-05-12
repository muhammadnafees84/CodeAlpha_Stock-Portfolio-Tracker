print("------------Stock Portfolio Tracker------------ ")
stocks = {
    "AAPL" : 180,
    "TSLA" : 250,
    "AMZN" : 150,
}
total_investment = 0
file = open("Portfolio_Stacks.csv","w")
file.write("Stock Name, Stock Price, Quantity, Investment\n")
num = int(input("Enter the number of stocks you want to track: "))
for i in range(num):
    stock_name = input("Enter the name of stock : ").upper()
    if stock_name in stocks:
        quantity = int(input("Enter the quantity of stocks : "))
        price = stocks[stock_name]
        investment = price * quantity
        total_investment = total_investment + investment
        print("Stock Price : ",price)
        print("Investment : ",investment)
        file.write(f"{stock_name}, {price}, {quantity}, {investment}\n")
    else:
        print("Stock not found in the portfolio.")
print("Total Investment : ",total_investment)
