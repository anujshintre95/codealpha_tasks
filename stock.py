# ============================================
# CodeAlpha Internship Project
# Project: Stock Portfolio Tracker
# Author: Anuj Shintre
# ============================================

# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320,
    "AMZN": 150
}

portfolio = {}
total_value = 0

print("=" * 50)
print("📈 Welcome to Stock Portfolio Tracker")
print("=" * 50)

# Number of different stocks
while True:
    try:
        num_stocks = int(input("How many different stocks do you own? "))
        if num_stocks > 0:
            break
        else:
            print("Please enter a number greater than 0.")
    except ValueError:
        print("Please enter a valid number.")

# Input stock details
for i in range(num_stocks):

    print(f"\nStock {i+1}")

    stock = input("Enter Stock Symbol (AAPL, TSLA, etc.): ").upper()

    if stock not in stock_prices:
        print("❌ Stock not found in database!")
        continue

    while True:
        try:
            quantity = int(input("Enter Quantity: "))
            if quantity > 0:
                break
            else:
                print("Quantity must be greater than 0.")
        except ValueError:
            print("Please enter a valid quantity.")

    price = stock_prices[stock]
    investment = price * quantity

    portfolio[stock] = {
        "Price": price,
        "Quantity": quantity,
        "Investment": investment
    }

    total_value += investment

# Display Portfolio
print("\n")
print("=" * 50)
print("YOUR STOCK PORTFOLIO")
print("=" * 50)

for stock, details in portfolio.items():

    print(f"""
Stock Symbol : {stock}
Price        : ₹{details['Price']}
Quantity     : {details['Quantity']}
Investment   : ₹{details['Investment']}
------------------------------------------
""")

print("=" * 50)
print(f"💰 Total Portfolio Value = ₹{total_value}")
print("=" * 50)

# Save Report
with open("portfolio.txt", "w", encoding="utf-8") as file:

    file.write("STOCK PORTFOLIO REPORT\n")
    file.write("=" * 40 + "\n\n")

    for stock, details in portfolio.items():

        file.write(f"""Stock Symbol : {stock}
Price        : ₹{details['Price']}
Quantity     : {details['Quantity']}
Investment   : ₹{details['Investment']}
----------------------------------------
""")

    file.write(f"\nTotal Portfolio Value = ₹{total_value}")

print("\n✅ Portfolio report saved successfully as 'portfolio.txt'")
print("Thank you for using Stock Portfolio Tracker!")