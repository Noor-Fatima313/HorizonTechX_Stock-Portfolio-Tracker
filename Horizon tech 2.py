# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 135
}

portfolio = {}
total_value = 0

print("===== Stock Portfolio Tracker =====")
print("Available Stocks:")
for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")

# Number of different stocks
num_stocks = int(input("\nHow many different stocks do you own? "))

# User input
for i in range(num_stocks):
    stock_name = input(f"\nEnter stock {i+1} symbol: ").upper()

    if stock_name in stock_prices:
        quantity = int(input(f"Enter quantity of {stock_name}: "))
        portfolio[stock_name] = quantity
    else:
        print("Stock not found! Skipping...")

# Calculate total investment
print("\n===== Portfolio Summary =====")
for stock, quantity in portfolio.items():
    value = stock_prices[stock] * quantity
    total_value += value
    print(f"{stock}: {quantity} shares × ${stock_prices[stock]} = ${value}")

print(f"\nTotal Investment Value: ${total_value}")

# Save results to a text file
with open("portfolio_summary.txt", "w") as file:
    file.write("===== Portfolio Summary =====\n")
    for stock, quantity in portfolio.items():
        value = stock_prices[stock] * quantity
        file.write(f"{stock}: {quantity} shares × ${stock_prices[stock]} = ${value}\n")
    file.write(f"\nTotal Investment Value: ${total_value}")

print("\nPortfolio summary has been saved to 'portfolio_summary.txt'.")