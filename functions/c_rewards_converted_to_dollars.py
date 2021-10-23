import pandas as pd


def rewardsConvertedToDollars():

    rewards_path = "converted_data/summed_rewards_by_epoch.csv"
    epoch_prices_path = "converted_data/epoch_market_prices.csv"

    rewards_df = pd.read_csv(rewards_path)
    prices_df = pd.read_csv(epoch_prices_path)

    merged_df = pd.merge(rewards_df, prices_df)
    merged_df["usd"] = merged_df["amount"] * merged_df["market_price"]
    merged_df.to_csv("converted_data/rewards_converted_to_dollars.csv")
    print(merged_df)


rewardsConvertedToDollars()
