from blockfrost import BlockFrostApi, ApiError
from dotenv import load_dotenv
import os
import pandas as pd
import json

load_dotenv()
PROJECT_ID = os.getenv("PROJECT_ID")


def getStakingAddresses():

    # Read the CSV file with pandas.
    df = pd.read_csv("addresses/epochs.csv")

    # Iterate over the dataframe rows.
    for index, address in df.iterrows():
        print(index, address)
        getStakingRewards(address)


def getStakingRewards(address: str):

    row_list = []

    # API call to request data.
    api = BlockFrostApi(
        project_id=PROJECT_ID
    )

    try:
        request = api.epoch(address["epoch"])
        row_list.append(request)
        df = pd.read_csv("epoch_data/epoch_data.csv", index_col=[0])
        request_df = pd.DataFrame(row_list)
        append_df = df.append(request_df)
        append_df.to_csv("epoch_data/epoch_data.csv")
        print(append_df)

    except ApiError as e:
        print(e)


getStakingAddresses()
