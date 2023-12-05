import pandas as pd
import os
address="/Sleep/Sleep_data/"
df=pd.DataFrame()
directory = os.fsencode(address)
for filename in os.listdir(directory):
    with open(os.path.join(directory, filename)) as f:
            d=pd.read_json(f)
            id=filename[7:9]
            id=id.decode('UTF-8')
            d.insert(0,'ID',id)
            df=pd.concat([df, d], ignore_index=True)
df = df.dropna(thresh=6)
df = df.drop('null', axis=1)
df.reset_index(inplace=True, drop=True)
print(df)