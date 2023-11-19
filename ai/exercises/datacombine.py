import pandas as pd

dfa1 = pd.read_csv('archedback1.csv')
dfa2 = pd.read_csv('archedback2.csv')
dfc1 = pd.read_csv('correct1.csv')
dfc2 = pd.read_csv('correct2.csv')
dfe1 = pd.read_csv('elbowsbent1.csv')
dfe2 = pd.read_csv('elbowsbent2.csv')
dfk1 = pd.read_csv('kneebent1.csv')
dfk2 = pd.read_csv('kneebent2.csv')

combined_df = pd.concat([dfa1, dfa2, dfc1, dfc2, dfe1, dfe2, dfk1, dfk2], ignore_index=True)
combined_df_shuffled = combined_df.sample(frac=1).reset_index(drop=True)
combined_df_shuffled.to_csv('pushup_data.csv', index=False)