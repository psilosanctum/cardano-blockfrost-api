import pandas as pd
import glob


def totalStakingRewardsByEpoch():

    # Designate directory subject to iteration.
    path = "raw_rewards/"
    all_files = glob.glob(path + "*.csv")

    # Create empty list that will be used to append dataframes from iteration.
    new_df = []

    # Iterate over directory and append dataframes to the empty list.
    for filename in all_files:
        df = pd.read_csv(filename, index_col=[0])
        new_df.append(df)

    # Create dataframe in new variable.
    frame = pd.concat(new_df, axis=0, ignore_index=True)

    # Group rows by epoch and sum the values of each epoch.
    frame = frame.groupby('epoch').sum()

    # Convert from lovelaces unit.
    frame['amount'] = frame['amount']/1000000

    # Store as a new file.
    frame.to_csv("converted_data/summed_rewards_by_epoch.csv")

    print(frame)


totalStakingRewardsByEpoch()
