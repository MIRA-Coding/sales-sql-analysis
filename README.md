# Sales SQL Analysis

A small SQL project that answers 13 business questions on a 3-table sales dataset
(customers, products, orders): revenue by city, best customer, products never sold, and more.

## What I did
- Built the database with a Python script (`setup_db.py`) so anyone can recreate it.
- Wrote each question as a separate query in `queries/`.
- Checked every result against the total revenue (16,750) to catch JOIN mistakes.

## How to run

Requires Python 3 and the `sqlite3` command-line tool
(preinstalled on macOS; on Windows, install it from sqlite.org).
Run the commands from the project root.

```bash
python setup_db.py        # use python3 on macOS/Linux if needed
sqlite3 -header -column sales.db ".read queries/04_total_profit_by_city.sql"
```

Or open any `.sql` file in VS Code with the SQLTools extension and click **Run**.

## Example result
| city | profit_of_city |
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