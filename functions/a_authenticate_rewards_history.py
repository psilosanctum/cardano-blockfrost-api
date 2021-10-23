from blockfrost import BlockFrostApi, ApiError
from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()
PROJECT_ID = os.getenv("PROJECT_ID")


def getStakingAddresses():

    # Read the CSV file with pandas.
    df = pd.read_csv("addresses/stake_address.csv")

    # Iterate over the dataframe rows.
    for index, address in df.iterrows():
        print(index, address)
        getStakingRewards(address)


def getStakingRewards(address: str):

    # Create an empty list that will be used to append the API responses.
    epoch_list = []
    amount_list = []
    pool_list = []

    # API call to request data.
    api = BlockFrostApi(
        project_id=PROJECT_ID
    )

    try:
        request = api.account_rewards(address['stake_address'])
        for i in request:
            epoch_list.append(i.epoch)
            amount_list.append(i.amount)
            pool_list.append(i.pool_id)

        df = pd.read_csv(
            "addresses/template.csv".format(address['account']), index_col=[0])
        df['amount'] = amount_list
        df['epoch'] = epoch_list
        df['pool_id'] = pool_list
        df.to_csv("raw_rewards/{}.csv".format(address['account']))
        print(df)

    except ApiError as e:
        print(e)

    # Old API
        # try:
    #     response = api.account_rewards(
    #         address['stake_address'])
    #     print(response)

    #     for project in response:
    #         itemDict = {}
    #         itemDict.update(project)
    #         row_list.append(itemDict)

    #     df = pd.DataFrame(row_list)
    #     df.to_csv("raw_rewards/" +
    #               "{}.csv".format(address['account']))

    # except ApiError as e:
    #     print(e)


getStakingAddresses()
