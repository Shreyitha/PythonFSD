def calculate_total_profit(products):
   # Calculate the total profit made across all products.
    overall_total_profit = 0

    for product in products:
        cost_price = product["cost_price"]
        sell_price = product["sell_price"]
        inventory = product["inventory"]

        total_cost = cost_price * inventory
        total_revenue = sell_price * inventory
        total_profit = total_revenue - total_cost

        overall_total_profit += total_profit

    # Round the overall total profit to the nearest dollar
    rounded_total_profit = round(overall_total_profit)

    return rounded_total_profit

# Example usage:
products_data = [
    {"product_name": "Product A", "cost_price": 5.5, "sell_price": 8.5, "inventory": 100},
    {"product_name": "Product B", "cost_price": 3.0, "sell_price": 6.0, "inventory": 150},
    {"product_name": "Product C", "cost_price": 2.5, "sell_price": 4.0, "inventory": 200},
]

total_profit = calculate_total_profit(products_data)
print(f"Overall Total Profit: ${total_profit}")
