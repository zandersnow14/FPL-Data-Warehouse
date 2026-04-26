.PHONY: ingest extract verify lint

ingest:
	uv run python ingestion/main.py

extract:
	uv run python ingestion/src/extract.py

verify:
	uv run python scripts/verify_bronze.py

lint:
	uv run ruff check .

lint-format:
	uv run ruff format --check .

inspect-bronze:
	uv run python scripts/inspect_bronze.py

dbt-run:
	cd dbt/fpl_dbt && uv run dbt run

dbt-test:
	cd dbt/fpl_dbt && uv run dbt test