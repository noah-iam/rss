import pandas as pd
import sys
print(sys.path)



# Specify the path to your CSV file
csv_file_path = "e:\\Projects\\dailybuzzrnews\\rss\\rss\\nlp\\data\\rss-feed_22-01-2023.csv"

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv(csv_file_path)
print(df.columns)
count = 0
for index, row in df.iterrows():
    if count == 2:
        print(row['text'])
        print(row['link'])
    count = count + 1
