import sqlite3

conn = sqlite3.connect("sales.db")
cur = conn.cursor()

cur.executescript("""
DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS orders;

CREATE TABLE customers (id INTEGER, name TEXT, city TEXT, signup_date TEXT);
CREATE TABLE products  (id INTEGER, name TEXT, category TEXT, price INTEGER);
CREATE TABLE orders    (id INTEGER, customer_id INTEGER, product_id INTEGER, qty INTEGER, order_date TEXT);

INSERT INTO customers VALUES
 (1,'Amera','Cairo','2025-11-01'),
 (2,'Sara','Giza','2025-11-15'),
 (3,'Khaled','Alexandria','2025-12-02'),
 (4,'Laila','Cairo','2025-12-20'),
 (5,'Omar','Alexandria','2026-01-03');

INSERT INTO products VALUES
 (1,'Laptop','Electronics',3500),
 (2,'Mouse','Accessories',150),
 (3,'Monitor','Electronics',900),
 (4,'Keyboard','Accessories',250),
 (5,'Webcam','Accessories',400);

INSERT INTO orders VALUES
 (1,1,1,2,'2026-01-05'),
 (2,2,2,5,'2026-01-06'),
 (3,1,3,3,'2026-01-07'),
 (4,3,4,4,'2026-02-08'),
 (5,4,1,1,'2026-02-09'),
 (6,2,3,2,'2026-02-10');
""")
conn.commit()
conn.close()
print(" sales.db created successfully with tables: customers, products, and orders.")