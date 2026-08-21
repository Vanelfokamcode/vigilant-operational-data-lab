"""Load local JSONL operational events into DuckDB."""

from pathlib import Path

import duckdb

PROJECT_ROOT = Path(__file__).resolve().parents[1]
EVENT_LOG_PATH = PROJECT_ROOT / "data" / "raw" / "order_events.jsonl"
DUCKDB_PATH = PROJECT_ROOT / "data" / "vigilant_ops.duckdb"


def main() -> None:
    if not EVENT_LOG_PATH.exists():
        raise SystemExit(
            "No event log found. Run pytest first or create an order through the API."
        )

    DUCKDB_PATH.parent.mkdir(parents=True, exist_ok=True)

    with duckdb.connect(str(DUCKDB_PATH)) as connection:
        connection.execute("DROP TABLE IF EXISTS raw_order_events")
        connection.execute(
            """
            CREATE TABLE raw_order_events AS
            SELECT *
            FROM read_json_auto(?, format = 'newline_delimited')
            """,
            [str(EVENT_LOG_PATH)],
        )

        event_count = connection.execute(
            "SELECT count(*) FROM raw_order_events"
        ).fetchone()[0]

    print(f"Loaded {event_count} event(s) into {DUCKDB_PATH}")


if __name__ == "__main__":
    main()
