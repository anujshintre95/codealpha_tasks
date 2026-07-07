import csv

# ==========================================
#     STOCK PORTFOLIO TRACKER
#        CodeAlpha Internship
# ==========================================

STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320,
    "AMZN": 150,
    "NVDA": 450,
    "META": 290
}


def display_header():
    print("=" * 50)
    print("📈 STOCK PORTFOLIO TRACKER")
    print("=" * 50)


def get_number():
    while True:
        try:
            num = int(input("\nHow many different stocks do you own? "))
            if num > 0:
                return num
            else:
                print("Enter a number greater than 0.")
        except ValueError:
            print("Invalid input! Enter a valid number.")


def get_quantity():
    while True:
        try:
            qty = int(input("Enter Quantity: "))
            if qty > 0:
                return qty
            else:
                print("Quantity must be greater than 0.")
        except ValueError:
            print("Enter a valid quantity.")


def collect_portfolio():

    portfolio = {}

    total = 0

    count = get_number()

    for i in range(count):

        print(f"\nStock {i+1}")

        symbol = input("Enter Stock Symbol: ").upper().strip()

        if symbol not in STOCK_PRICES:
            print("❌ Stock not available.")
            continue

        quantity = get_quantity()

        price = STOCK_PRICES[symbol]

        investment = price * quantity

        portfolio[symbol] = {
            "Price": price,
            "Quantity": quantity,
            "Investment": investment
        }

        total += investment

    return portfolio, total


def display_portfolio(portfolio, total):

    print("\n")
    print("=" * 55)
    print("YOUR PORTFOLIO")
    print("=" * 55)

    if not portfolio:
        print("No valid stocks entered.")
        return

    for stock, details in portfolio.items():

        print(f"""
Stock Symbol : {stock}
Price        : ₹{details['Price']}
Quantity     : {details['Quantity']}
Investment   : ₹{details['Investment']}
---------------------------------------------
""")

    print("=" * 55)
    print(f"💰 Total Portfolio Value : ₹{total}")
    print("=" * 55)


def save_txt(portfolio, total):

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

        file.write(f"\nTotal Portfolio Value : ₹{total}")

    print("\n✅ portfolio.txt created successfully.")


def save_csv(portfolio):

    with open("portfolio.csv", "w", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        writer.writerow(["Stock", "Price", "Quantity", "Investment"])

        for stock, details in portfolio.items():

            writer.writerow([
                stock,
                details["Price"],
                details["Quantity"],
                details["Investment"]
            ])

    print("✅ portfolio.csv created successfully.")


def main():

    display_header()

    portfolio, total = collect_portfolio()

    display_portfolio(portfolio, total)

    if portfolio:
        save_txt(portfolio, total)
        save_csv(portfolio)

    print("\n🎉 Thank you for using Stock Portfolio Tracker!")


if __name__ == "__main__":
    main()