def calculate_total_profit(products_data):
    total_profit = sum((p["sell_price"] - p["cost_price"]) * p["inventory"] for p in products_data)
    return round(total_profit)


products_data = [
    {"product_name": "Product A", "cost_price": 5.5, "sell_price": 8.5, "inventory": 100},
    {"product_name": "Product B", "cost_price": 3.0, "sell_price": 6.0, "inventory": 150},
    {"product_name": "Product C", "cost_price": 2.5, "sell_price": 4.0, "inventory": 200},
]

total_profit = calculate_total_profit(products_data)
print(f"Total Profit: ${total_profit}")
