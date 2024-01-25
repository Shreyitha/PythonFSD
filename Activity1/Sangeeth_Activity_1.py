#Given_Data
products_data = [
    {"product_name": "Product A", "cost_price": 5.5, "sell_price": 8.5, "inventory": 100},
    {"product_name": "Product B", "cost_price": 3.0, "sell_price": 6.0, "inventory": 150},
    {"product_name": "Product C", "cost_price": 2.5, "sell_price": 4.0, "inventory": 200},]

total_profit=0

#profit_calculation
for i in products_data:
    profit= (i['sell_price']-i['cost_price'])* i['inventory']
    print(i['product_name']+" with "+ str(i['inventory'])+ " units of inventory, returns a profit of: $"+ str(round(profit)))
    total_profit+=profit

print("Total profit obtained for the company is: $" + str(round(total_profit)))    