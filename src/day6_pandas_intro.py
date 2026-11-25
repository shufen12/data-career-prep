import pandas as pd
# df = pd.read_csv('data/cars_sample.csv')
# print(df.head(3))
# print(df.shape)
# print(df.columns)
# print(df.info())


df_sensors = pd.read_csv('data/sensor_log.txt',sep='\t',names=['frame_id','speed_kmh','weather','is_brake'])
print(df_sensors)


# price_s = df['price_wan']
# print(type(price_s))
# print(f"{price_s.mean():.2f}")
# sub_df = df[['price_wan','brand']]
# print(type(sub_df))
# print(sub_df.head(3))