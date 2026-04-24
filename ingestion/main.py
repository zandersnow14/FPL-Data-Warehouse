
import datetime

from src.extract import get_bootstrap_data, get_fixture_data
from src.load import load_bronze_table


def main():
    """
    Main function.

    :returns: nothing yet
    """

    ingested_at = datetime.datetime.now(datetime.UTC)

    bootstrap_data = get_bootstrap_data()
    fixture_data = get_fixture_data() 

    load_bronze_table("players", bootstrap_data['players'], ingested_at)
    load_bronze_table("gameweeks", bootstrap_data['gameweeks'], ingested_at)
    load_bronze_table("teams", bootstrap_data['teams'], ingested_at)
    load_bronze_table("positions", bootstrap_data['positions'], ingested_at)
    load_bronze_table("fixtures", fixture_data, ingested_at)


if __name__ == "__main__":
    main()

