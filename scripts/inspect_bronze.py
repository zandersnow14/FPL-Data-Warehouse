import duckdb
import json

tables = ["players", "teams", "gameweeks", "positions", "fixtures"]

conn = duckdb.connect("data/fpl_local.duckdb")

for table in tables:

    row = conn.execute(f"select payload from bronze.{table} limit 1").fetchone()[0]
    print(f"Table: {table}")
    print(json.loads(row))
    print("\n")
conn.close()