import pandas as pd
import glob
from os import listdir
import random
from pathlib import Path



def find_csv_filenames( path_to_dir, suffix=".csv" ):
    filenames = listdir(path_to_dir)
    return [ filename for filename in filenames if filename.endswith( suffix ) ]


csv_files = find_csv_filenames("C:/Users/eunoia/Desktop/Coding_Projects/COP3530/SameSampMaster/SpotifyDataCollector/spotified_csvs")

def playcountGenerator(row):
   if row['popularity'] <= 20:
        return random.randint(10000,100000)
   elif 20 < row['popularity'] <= 50:
       return random.randint(100000,500000)
   elif 50 < row['popularity'] <= 80:
       return random.randint(500000,10000000)
   elif 80 < row['popularity'] <= 100:
       return random.randint(10000000,1000000000)
   
def revenueGenerator(row):
    return int(row['playCount'] * 0.002)
def ageCalc(row):
    return int(2023 - int(row['year']))
def annualRev(row):
    if row['age'] <= 8 and row['age'] != 0: 
        return int(row['grossRev'] / row['age'])
    else:
        return row['grossRev'] / 8
   
   
df_csv_concat = pd.concat([pd.read_csv(f'C:/Users/eunoia/Desktop/Coding_Projects/COP3530/SameSampMaster/SpotifyDataCollector/spotified_csvs/{file}') for file in csv_files ], ignore_index=True)



df_csv_concat["playCount"] = df_csv_concat.apply(playcountGenerator, axis=1)
df_csv_concat["grossRev"] = df_csv_concat.apply(revenueGenerator, axis=1)
df_csv_concat["age"] = df_csv_concat.apply(ageCalc, axis=1)
df_csv_concat["annualRev"] = df_csv_concat.apply(annualRev, axis=1)
df_csv_concat.head(5)

df_csv_concat.to_csv('C:/Users/eunoia/Desktop/Coding_Projects/COP3530/SameSampMaster/SpotifyDataCollector/spotified_csvs/concat.csv')

# folder = "C:/Users/eunoia/Desktop/Coding_Projects/COP3530/SameSampMaster/SpotifyDataCollector/test"
# for file in Path(folder).glob('*.csv'):
#     df = pd.read_csv(file)
#     df["playCount"] = df.apply(playcountGenerator, axis=1)
#     df["grossRev"] = df.apply(revenueGenerator, axis=1)
#     df["age"] = df.apply(ageCalc, axis=1)
#     df["annualRev"] = df.apply(annualRev, axis=1)

#     df.to_csv(file.with_suffix('.csv'), index = False)

print('finished')

