import pandas as pd
df=pd.read_csv("weatherPastWeekDelhi")
pd.set_option("display.max_columns", None)
df_dict=df.to_dict()
df_list=df["Remarks"].tolist()
print(df_list)