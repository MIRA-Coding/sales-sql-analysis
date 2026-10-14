
#       ----------------------- 1: loops on data structures -----------------------

from matplotlib.colors import cnames


numbers= [1,2,3]

print(numbers[0:], len(numbers))

total=0
for num in numbers:
    total+=num
    print( total)
    if total!=6:
        print("not yet")
    else: 
        print("total is 6")
    
numbers.append(4)
print(numbers)


#       ----------------------- 2: working with lists and dictionaries -----------------------

grades = [85, 92, 78]

for g in grades:
    print(g)

for i, g in enumerate(grades):     # مع الفهرس
    print(i, g)

for name, grade in zip(cnames, grades):
    print(name, grade)

retries = 0
while retries < 3:
    print("try", retries)
    retries += 1


#    ----------------------- 3: working with dictionaries -----------------------

orders = [
    {"id": 1, "product": "Laptop",   "price": 3500, "qty": 2, "city": "Cairo"},
    {"id": 2, "product": "Mouse",    "price": 150,  "qty": 5, "city": "Giza"},
    {"id": 3, "product": "Monitor",  "price": 900,  "qty": 3, "city": "Cairo"},
    {"id": 4, "product": "Keyboard", "price": 250,  "qty": 4, "city": "Alex"},
]

total_price = 0
max_line_total = None
best_product = None
city_totals = {}

print(f"{'Product':<10} => TotalPrice")
for order in orders:
    line_total = order["price"] * order["qty"]      # تُحسب مرة واحدة فقط
    print(f"{order['product']:<10} => {line_total}")

    total_price += line_total

    if max_line_total is None or line_total > max_line_total:
        max_line_total = line_total
        best_product = order["product"]

    city = order["city"]
    city_totals[city] = city_totals.get(city, 0) + line_total

print("\nTotal Price:", total_price)
print("Average of order:", total_price / len(orders))
print("Best Product:", best_product, "-", max_line_total)
print("City Totals:", city_totals)


#     ----------------------- 4: working with zip() -----------------------

names  = ["Amera", "Sara", "Khaled"]
grades = [95, 72, 88]
z = zip(names, grades)
print(list(z))    # [('Amera',95), ('Sara',72), ('Khaled',88)]
print(list(z))


#   ----------------------- 5: working with sqlite3 connected with real db --------

import sqlite3

conn = sqlite3.connect("sales.db")
cur = conn.cursor()

cur.execute("SELECT * FROM orders WHERE qty > 2")

for row in cur.fetchall():
    print(row)

conn.close()
