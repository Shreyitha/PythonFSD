def calculate_total_profit(products_data):
    
    total_profit = 0

    
    for product in products_data:
    
        profit = (product["sell_price"] - product["cost_price"]) * product["inventory"]

        
        total_profit += profit

    
    rounded_total_profit = round(total_profit)

    
    return rounded_total_profit

products_data = [
    {"product_name": "Product A", "cost_price": 5.5, "sell_price": 8.5, "inventory": 100},
    {"product_name": "Product B", "cost_price": 3.0, "sell_price": 6.0, "inventory": 150},
    {"product_name": "Product C", "cost_price": 2.5, "sell_price": 4.0, "inventory": 200},
]

result = calculate_total_profit(products_data)
print(f"Total Profit: ${result}")
