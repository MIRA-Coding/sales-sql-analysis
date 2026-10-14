# Sales SQL Analysis

A small SQL project that answers 7 business questions on a 3-table sales dataset
(customers, products, orders): revenue by city, best customer, products never sold, and more.

## What I did
- Built the database with a Python script (`setup_db.py`) so anyone can recreate it.
- Wrote each question as a separate query in `queries/`.
- Checked every result against the total revenue (16,750) to catch JOIN mistakes.

## How to run
```bash
python setup_db.py
sqlite3 sales.db < queries/02_revenue_by_city.sql
```

## Example result
| city | revenue |
|---|---|
| Cairo | 13200 |
| Giza | 2550 |
| Alexandria | 1000 |

## What I learned
- LEFT JOIN + IS NULL finds rows with no match (customers who never ordered).
- A JOIN can multiply rows, so I compare COUNT(*) before and after.
- A query returning "top 1" needs ORDER BY ... DESC, otherwise it returns an arbitrary row.

## Next steps
- Load the same data from CSV and from S3.