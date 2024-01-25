def total_profit(productdata):
  profits=[(product["sell_price"]-product["cost_price"])*product["inventory"]  for product in productdata]
  totalprofit=round(sum(profits))

  [print("Profit Obtained from {} : ${}".format(productdata[i]["product_name"],round(profits[i]))) for i in range(len(profits))]
  return totalprofit

products_data = [
    {"product_name": "Product A", "cost_price": 5.5, "sell_price": 8.5, "inventory": 100},
    {"product_name": "Product B", "cost_price": 3.0, "sell_price": 6.0, "inventory": 150},
    {"product_name": "Product C", "cost_price": 2.5, "sell_price": 4.0, "inventory": 200},
]
print("Total Profit Obtained from manufacturing company is : ${}".format(total_profit(products_data)))