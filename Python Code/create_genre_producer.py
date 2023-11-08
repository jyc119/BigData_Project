import pandas as pd
import numpy as np
import sys

print(sys.version)
print('pandas version', pd.__version__)
pd.set_option('display.max_columns', 500)

def create_df(s):
    df = pd.read_csv(r'C:\Users\jorda\OneDrive\Desktop\CS RIT\Intro to Big Data\Project\AnimeList.csv')
    df[s] = df[s].str.split(',')
    df = df.explode(s)

    unique_values = df[s].unique()
    cur_df = pd.DataFrame({s: unique_values})
    cur_df[s] = cur_df[s].replace('\\N', float('nan'))
    df_genres = cur_df.dropna()
    df_genres = df_genres.reset_index(drop=True)

    # Display the new DataFrame
    df_genres.index += 1
    df_genres.index.name = 'id'
    df_genres['id'] = df_genres.index

    print(df_genres)

create_df("genre")
create_df("producer")