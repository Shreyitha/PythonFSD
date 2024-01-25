def calculate_total_profit(products_data):
    # Initialize the total profit to zero
    Total_profit = 0

    # Loop through each product in the products_data list
    for product in products_data:
        # Calculate the profit for the individual product
        individual_profit = (product["sell_price"] - product["cost_price"]) * product["inventory"]

        # Add the individual profit to the total profit
        Total_profit += individual_profit

        # Print the individual profit for the current product
        print(str(product["product_name"] + ": $" + str(round(individual_profit))))

    # Return the total profit rounded to the nearest dollar
    return round(Total_profit)

# List of products with their details
products_data = [
    {"product_name": "Product A", "cost_price": 5.5, "sell_price": 8.5, "inventory": 100},
    {"product_name": "Product B", "cost_price": 3.0, "sell_price": 6.0, "inventory": 150},
    {"product_name": "Product C", "cost_price": 2.5, "sell_price": 4.0, "inventory": 200},
]

# Call the function to calculate total profit
Total_profit = calculate_total_profit(products_data)

# Print the total profit
print("Total profit: $" + str(Total_profit))
