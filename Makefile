.PHONY: ingest extract

ingest:
	uv run python ingestion/main.py

extract:
	uv run python ingestion/src/extract.py

verify:
	uv run python scripts/verify_bronze.py