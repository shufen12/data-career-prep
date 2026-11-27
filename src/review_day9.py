import pandas as pd
def analyze_sensor_log(file_path):
    try:
        df = pd.read_csv(file_path,header=None,names=['frame_id','speed','weather','is_anomaly'],sep='\t')
        print(df[(df['weather'] == '晴天') & (df['speed'] > 50)])
        hit = df['is_anomaly'].rolling(2).sum() == 2
        if hit.any():
            print(df.loc[hit, 'frame_id'])
        else:
            print('无连续异常帧')

    except FileNotFoundError:
        print("文件未找到")

analyze_sensor_log('data/sensor_log.txt')
analyze_sensor_log('data/missing.txt')

