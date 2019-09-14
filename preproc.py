import os
import pandas as pd
import math

def abs_delta(arr):
    return [arr[i + 1] - arr[i] for i in range(len(arr) - 1)]

def ratio_delta(arr):
    assert all(arr)
    return [arr[i + 1] / arr[i] - 1 for i in range(len(arr) - 1)]

def log_delta(arr):
    assert all(arr)
    return [math.log(arr[i + 1]) - math.log(arr[i]) for i in range(len(arr) - 1)]

def delta_trans(df, fn, cols):
    key_lookup = dict()
    for key in list(df):
        if key in cols:
            #print(len(fn(df[key])))
            key_lookup[key] = fn(df[key])
        else:
            key_lookup[key] = df[key][:-1]
        #print(len(key_lookup[key]))
    #print(len(key_lookup))
    #print(df.index)
    return pd.DataFrame(key_lookup, df.index[:-1])

df_list = []
for file in os.listdir("./"):
    if ".csv" in file:
        #print(pd.read_csv(file))
        df_list.append(pd.read_csv(file))

if __name__ == "__main__":
    df = pd.concat(df_list, axis=1)
    df = df.loc[:,~df.columns.duplicated()]
    df.rename(columns={"Unnamed:0":"Date"})
    df.to_csv("rate_1719.csv")
    
    df = pd.read_csv("rate_1719.csv")
    df.set_index('Date', inplace=True)
    
    df = df.drop(['Unnamed: 0'], axis=1)
    
    df.to_csv("rate_1719.csv")
    
    df_log = delta_trans(df, log_delta, list(df)[1:])
    
    df_log.to_csv("rate_delta.csv")
