import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns
import matplotlib.pyplot as plt

def time_varible_constractor(df):
    df['week_day']=df.date.dt.day_of_week+1
    df['year'] = df.date.dt.year
    df['month'] = df.date.dt.month
    df['year_day'] = df.date.dt.day_of_year
    df['day_name'] = df.date.dt.day_name()
    # 0: Winter - 1: Spring - 2: Summer - 3: Fall
    df["season"] = np.where(df.month.isin([12,1,2]), 0, 1)
    df["season"] = np.where(df.month.isin([6,7,8]), 2, df["season"])
    df["season"] = pd.Series(np.where(df.month.isin([9, 10, 11]), 3, df["season"])).astype("int8")
    return df
def holiday_merger(df,national,regional,local,events,work_day):
    print("length before: ",len(df))
    df = pd.merge(df, national, how = "left",on = ["date"])
    df = pd.merge(df, regional, how = "left", on = ["date", "state"])
    df = pd.merge(df, local, how = "left", on = ["date", "city"])
    df = pd.merge(df,work_day[["date", "type"]].rename({"type":"IsWorkDay"}, axis = 1),how = "left")
    df = pd.merge(df, events, how = "left")
    print("length affter: ",len(df))
    return df