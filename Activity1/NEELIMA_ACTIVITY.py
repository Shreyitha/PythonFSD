def calculate_total_profit(products_data):
    # Step 1: Initialize Total Profit
    total_profit = 0

    # Step 2: Iterate Through Products
    for product in products_data:
        # Step 3: Calculate Profit for Each Product
        profit = (product["sell_price"] - product["cost_price"]) * product["inventory"]

        # Step 4: Add Profit to Total
        total_profit += profit

    # Step 5: Round Total Profit
    rounded_total_profit = round(total_profit)

    # Step 6: Return Result
    return rounded_total_profit

# Example Usage
products_data = [
    {"product_name": "Product A", "cost_price": 5.5, "sell_price": 8.5, "inventory": 100},
    {"product_name": "Product B", "cost_price": 3.0, "sell_price": 6.0, "inventory": 150},
    {"product_name": "Product C", "cost_price": 2.5, "sell_price": 4.0, "inventory": 200},
]

result = calculate_total_profit(products_data)
print(f"Total Profit: ${result}")