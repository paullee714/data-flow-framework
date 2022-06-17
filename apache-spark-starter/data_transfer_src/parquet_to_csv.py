import pandas as pd

df = pd.DataFrame()
df.to_parquet("trip_data.parquet", compression="gzip")

df = pd.read_parquet("../data/fhvhv_tripdata_2021-03.parquet")
df.to_csv("../data/result_data/trip_data.csv")
