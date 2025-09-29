# Your stocks (you can change these)
my_stocks = {
    'AAPL': {'shares': 10, 'buy_price': 150.00},
    'GOOGL': {'shares': 5, 'buy_price': 2500.00}
}

# Current prices (you can change these)
current_prices = {
    'AAPL': 175.50,
    'GOOGL': 2700.25
}

total_spent = 0
total_value = 0

# Loop through each stock to find totals
for ticker, info in my_stocks.items():
    spent = info['shares'] * info['buy_price']
    value = info['shares'] * current_prices[ticker]

    total_spent += spent
    total_value += value

# Print the final results
print(f"Total spent: ${total_spent:.2f}")
print(f"Total worth: ${total_value:.2f}")
print(f"Total profit/loss: ${total_value - total_spent:.2f}")
