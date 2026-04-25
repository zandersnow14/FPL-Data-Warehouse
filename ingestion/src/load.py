
import datetime
import json
import os

import duckdb


def get_local_connection():
    """
    Gets a connection to a local duckdb database.

    :returns: Connection to duckdb database
    """
    os.makedirs("data", exist_ok=True)
    return duckdb.connect("data/fpl_local.duckdb")


def ensure_bronze_table(conn: duckdb.DuckDBPyConnection,
                        table_name: str) -> None:
    """
    Creates the bronze schema and table if they do not exist.

    :param conn: Connection to local duckdb database
    :param table_name: Table name to check
    :returns: None
    """

    sql = f"""
    CREATE SCHEMA IF NOT EXISTS bronze;
    CREATE TABLE IF NOT EXISTS bronze.{table_name} (
        ingested_at TIMESTAMP,
        payload VARCHAR
    );
    """

    conn.execute(sql)


def load_bronze_table(table_name: str,
                      records: list,
                      ingested_at: datetime.datetime) -> None:
    """
    Loads records into a table stored in a local duckdb database.

    :param table_name: Table name to load records into
    :param records: list of records to insert into the table
    :param ingested_at: the datetime (UTC) the data is inserted at
    :returns: None
    """

    conn = get_local_connection()

    sql = f"""
    INSERT INTO bronze.{table_name} (ingested_at, payload)
    VALUES (?, ?);
    """

    try:
        ensure_bronze_table(conn, table_name)

        rows = [(ingested_at, json.dumps(record))
                for record in records]

        conn.executemany(sql, rows)
    except Exception as e:
        print(f"Failed to load table {table_name}: {e}")
        raise
    finally:
        conn.close()
