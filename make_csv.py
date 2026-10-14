orders = [
    {"id": 1, "customer_id": 1, "product_id": 1, "qty": 2, "order_date": "2026-01-05"},
    {"id": 2, "customer_id": 2, "product_id": 2, "qty": 5, "order_date": "2026-01-06"},
    {"id": 3, "customer_id": 1, "product_id": 3, "qty": 3, "order_date": "2026-01-07"},
    {"id": 4, "customer_id": 3, "product_id": 4, "qty": 4, "order_date": "2026-02-08"},
    {"id": 5, "customer_id": 4, "product_id": 1, "qty": 1, "order_date": "2026-02-09"},
    {"id": 6, "customer_id": 2, "product_id": 3, "qty": 2, "order_date": "2026-02-10"},
]

# with open("orders.csv", "w", encoding="utf-8", newline="") as f:
#     f.write("id,customer_id,product_id,qty,order_date\n")
#     for o in orders:
#         f.write(f"{o['id']},{o['customer_id']},{o['product_id']},{o['qty']},{o['order_date']}\n")


# with open("orders.csv", encoding="utf-8") as f:
#     for line in f:
#         print(line.strip())


import csv

with open("orders2.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=["id", "customer_id", "product_id", "qty", "order_date"],
        
    )
    writer.writeheader()      # يكتب سطر الرؤوس
    writer.writerows(orders)  # يكتب كل الصفوف

with open("orders.csv", encoding="utf-8") as f:
    
    line = f.readline()
    print(repr(line))
    line = line.strip().split(",")
    print(line)
    for line in f:
        print(line.strip())

with open("orders.csv", encoding="utf-8") as f:
    header = f.readline().strip().split(",")   # سطر الرؤوس
    orders = []
    for line in f:
        values = line.strip().split(",")       # قيم السطر
        orders.append(dict(zip(header, values)))   # ← zip تربط الرأس بالقيمة!

print(orders[0])


with open("orders.csv", encoding="utf-8", newline="") as f:
    orders = list(csv.DictReader(f))

print(orders[0])
print("total orders: ", len(orders))

total_qty = 0
qty_per_customer = {}
for order in orders:
    total_qty += int(order["qty"])  # تحويل النص إلى عدد صحيح
    customer_id = order["customer_id"]
    qty_per_customer[customer_id] = qty_per_customer.get(customer_id, 0) + int(order["qty"])

print("total quantity: ", total_qty)
print("quantity per customer: ", qty_per_customer)

print(orders[0]["qty"])          # '2'      ← نص!
print(orders[0]["qty"] * 2)      # '22'     ← ⚠️ لا خطأ! فقط نتيجة خاطئة صامتة
print(int(orders[0]["qty"]) * 2) # 4        ← ✅ الصحيح 

import pandas as pd

df = pd.read_csv("orders.csv")
print(df.dtypes)                     # ← الأنواع استُنتجت تلقائياً، بلا int() واحدة
print(df["qty"].sum())               # ← المجمّع في كلمة
print(df.groupby("customer_id")["qty"].sum())   # ← GROUP BY