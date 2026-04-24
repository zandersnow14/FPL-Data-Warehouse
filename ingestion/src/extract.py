
import requests


BASE_URL = "https://fantasy.premierleague.com/api"
BOOTSTRAP_URL = f"{BASE_URL}/bootstrap-static"
FIXTURE_URL = f"{BASE_URL}/fixtures"


def get_bootstrap_data() -> dict:
    """
    Retrieves metadata about all elements of the FPL API.

    :returns: dict
    """
    res = requests.get(BOOTSTRAP_URL)
    res.raise_for_status()
    data = res.json()

    return {
        "teams":     data["teams"],
        "players":   data["elements"],
        "gameweeks": data["events"],
        "positions": data["element_types"]
    }


def get_fixture_data():
    
    res = requests.get(FIXTURE_URL)
    res.raise_for_status()
    return res.json()


if __name__ == "__main__":
    
    bootstrap_data = get_bootstrap_data()
    fixture_data = get_fixture_data()
