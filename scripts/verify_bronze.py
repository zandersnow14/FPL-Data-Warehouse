import duckdb

conn = duckdb.connect("data/fpl_local.duckdb")

tables = ["players", "teams", "gameweeks", "positions", "fixtures"]

for table in tables:
    count = conn.execute(f"select count(*) from bronze.{table}").fetchone()[0]
    latest = conn.execute(f"select max(ingested_at) from bronze.{table}").fetchone()[0]
    print(f"bronze.{table}: {count} rows, latest ingestion: {latest}")

conn.close()
