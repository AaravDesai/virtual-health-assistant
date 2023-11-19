import pandas as pd

df_hk1 = pd.read_csv('half_knees1.csv')
df_hk2 = pd.read_csv('half_knees2.csv')
df_sc1 = pd.read_csv('squatscorrect1.csv')
df_sc2 = pd.read_csv('squatscorrect2.csv')
df_kb1 = pd.read_csv('knee_bent1.csv')


combined_df = pd.concat([df_hk1, df_hk2, df_sc1, df_sc2, df_kb1], ignore_index=True)
combined_df_shuffled = combined_df.sample(frac=1).reset_index(drop=True)
combined_df_shuffled.to_csv('squats_data.csv', index=False)