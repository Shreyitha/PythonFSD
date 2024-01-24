products_data = [
    {"product_name": "Product A", "cost_price": 5.5, "sell_price": 8.5, "inventory": 100},
    {"product_name": "Product B", "cost_price": 3.0, "sell_price": 6.0, "inventory": 150},
    {"product_name": "Product C", "cost_price": 2.5, "sell_price": 4.0, "inventory": 200},
]
def Calc_profit(product_data):
    profit = 0
    
    for product in product_data:
        cost_price = product["cost_price"]
        sell_price = product["sell_price"]
        inventory = product["inventory"]
        
        profit_per_unit = sell_price - cost_price
        profit += profit_per_unit * inventory
    return round(profit)
    
total_profit = Calc_profit(products_data)
print("Total Profit is", total_profit)
