class manufacture_comp:
    def __init__(self,products_data):
        self.products_data=products_data

    def profit(self):
        total=0
        for x in self.products_data:
            profit=0
            product_name=x["product_name"]
            cost_price=x["cost_price"]
            sell_price=x["sell_price"]
            inventory=x["inventory"]
            profit=(sell_price-cost_price)*inventory
            total+=profit
        print("Total profit is ", total)
        return total
products_data = [
    {"product_name": "Product A", "cost_price": 5.5, "sell_price": 8.5, "inventory": 100},
    {"product_name": "Product B", "cost_price": 3.0, "sell_price": 6.0, "inventory": 150},
    {"product_name": "Product C", "cost_price": 2.5, "sell_price": 4.0, "inventory": 200},
]
a=manufacture_comp(products_data)
total_profit = a.profit()

