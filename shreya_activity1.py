products_data = [
    {"product_name": "Product A", "cost_price": 5.5, "sell_price": 8.5, "inventory": 100},
    {"product_name": "Product B", "cost_price": 3.0, "sell_price": 6.0, "inventory": 150},
    {"product_name": "Product C", "cost_price": 2.5, "sell_price": 4.0, "inventory": 200},
]


def total_profit_cal(products_data):
    total_profit=0
    for product in products_data:
        each_profit=product['sell_price']-product['cost_price']
        total_profit+=each_profit*product['inventory']

    return round(total_profit)
    

total_profit=total_profit_cal(products_data)
print(f'Total profit is : ${total_profit}')