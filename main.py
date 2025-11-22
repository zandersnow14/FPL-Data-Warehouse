
from datetime import datetime

import pandas as pd
import requests

BOOTSTRAP_URL = "https://fantasy.premierleague.com/api/bootstrap-static/"


def get_gameweek_data() -> pd.DataFrame:

    res = requests.get(BOOTSTRAP_URL)
    data: dict = res.json()
    gw_df = pd.DataFrame(data['events'])
    gw_df = gw_df[['id', 'name', 'deadline_time_epoch', 'finished', 'is_current', 'is_previous', 'is_next']]
    gw_df['deadline_time'] = gw_df['deadline_time_epoch'].apply(lambda x: datetime.fromtimestamp(x))
    return gw_df


def get_player_data() -> pd.DataFrame:

    res = requests.get(BOOTSTRAP_URL)
    data: dict = res.json()
    player_df = pd.DataFrame(data['elements'])
    player_df = player_df[['first_name', 'second_name', 'web_name', 'team', 'now_cost']]
    player_df['now_cost'] = player_df['now_cost'] / 10
    print(player_df)


def main():
    gw_data = get_gameweek_data()
    
    get_player_data()



if __name__ == "__main__":
    main()

