import pandas as pd

path = "epoch_data/epoch_data.csv"

df = pd.read_csv(path, index_col=[0])
df["output"] = df["output"]/1000000
df["fees"] = df["fees"]/1000000
df["active_stake"] = df["active_stake"]/1000000
df["avg_transaction_cost"] = df["fees"]/df["tx_count"]
print(df)

df.to_csv("epoch_data/converted_epoch_data.csv")
