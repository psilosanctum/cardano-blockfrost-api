import pandas as pd
import glob


def totalStakingRewardsByEpoch():

    path = "raw_rewards/"
    all_files = glob.glob(path + "*.csv")

    new_df = []

    for filename in all_files:
        df = pd.read_csv(filename, index_col=[0])
        new_df.append(df)

    frame = pd.concat(new_df, axis=0, ignore_index=True)
    frame = frame.groupby('epoch').sum()
    frame['amount'] = frame['amount']/1000000
    frame.to_csv("converted_data/summed_rewards_by_epoch.csv")

    print(frame)


totalStakingRewardsByEpoch()
