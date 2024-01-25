#!/usr/bin/env python
# coding: utf-8

# In[35]:


total_profit = 0

products_data = [
    {"product_name": "Product A", "cost_price": 5.5, "sell_price": 8.5, "inventory": 100},
    {"product_name": "Product B", "cost_price": 3.0, "sell_price": 6.0, "inventory": 150},
    {"product_name": "Product C", "cost_price": 2.5, "sell_price": 4.0, "inventory": 200},
]

for product in products_data:
    profit = (product["sell_price"] - product["cost_price"]) * product['inventory']
    
    total_profit += profit

#print("total profit is :", total_profit)

round_total = round(total_profit)

print(f"The Round Total profit is : ${round_total}")


# In[ ]:




