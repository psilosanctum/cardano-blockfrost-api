import pandas as pd


def rewardsConvertedToDollars():

    # Specify file paths of targeted data.
    rewards_path = "converted_data/summed_rewards_by_epoch.csv"
    epoch_prices_path = "converted_data/epoch_market_prices.csv"

    # Read the data into separate variables.
    rewards_df = pd.read_csv(rewards_path)
    prices_df = pd.read_csv(epoch_prices_path)

    # Merge the two dataframes into a single dataset.
    merged_df = pd.merge(rewards_df, prices_df)

    # Convert $ADA to USD.
    merged_df["usd"] = merged_df["amount"] * merged_df["market_price"]

    # Store the dataset as a new file.
    merged_df.to_csv("converted_data/rewards_converted_to_dollars.csv")
    print(merged_df)


rewardsConvertedToDollars()
