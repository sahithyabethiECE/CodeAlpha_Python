#  Stock Portfolio Tracker 
# Author: BETHI SAHITHYA VARSHINI

# Step 1: Hardcoded stock prices bro
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 130
}

portfolio = {}
total_investment = 0

print("📈 Stock Portfolio Tracker - CodeAlpha Task 2 📈")
print("Available stocks:", ", ".join(stock_prices.keys()))
while True:
    stock_name = input("\nEnter stock symbol (or 'done' to finish): ").upper()

    if stock_name == 'DONE':
        break

    if stock_name not in stock_prices:
        print("❌ Stock not found . Available:", ", ".join(stock_prices.keys()))
        continue

    try:
        quantity = int(input(f"Enter quantity for {stock_name}: "))
        if quantity <= 0:
            print("❌ Quantity should be greater than 0 ")
            continue
    except:
        print("❌ Valid number ")
        continue

    portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity
    print(f"✅ Added {quantity} shares of {stock_name}")
print("\n" + "="*40)
print("📊 YOUR PORTFOLIO SUMMARY 📊")
print("="*40)

for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = price * qty
    total_investment += value
    print(f"{stock}: {qty} shares x ${price} = ${value}")

print("-"*40)
print(f"💰 TOTAL INVESTMENT: ${total_investment}")
print("="*40)
save = input("\nSave to file? (yes/no): ").lower()
if save == 'yes':
    with open("portfolio_summary.txt", "w") as f:
        f.write("Stock Portfolio Summary\n")
        f.write("="*30 + "\n")
        for stock, qty in portfolio.items():
            f.write(f"{stock}: {qty} shares x ${stock_prices[stock]} = ${stock_prices[stock] * qty}\n")
        f.write(f"\nTotal Investment: ${total_investment}")
    print("✅ Saved to portfolio_summary.txt ")