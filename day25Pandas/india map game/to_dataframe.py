import pandas as pd
df=pd.DataFrame({'states': ['ladakh', 'kashmir', 'jammu', 'himachal pradesh', 'uttrakhand', 'uttar pradesh', 'bihar', 'sikkim', 'arunachal pradesh', 'assam', 'nagaland', 'manipur', 'mizoram', 'tripura', 'meghalaya', 'west bengal', 'jharkhand', 'bihar', 'orrisa', 'chhatisgarh', 'madhya pradesh', 'rajasthan', 'haryana', 'delhi', 'punjab', 'gujarat', 'maharashtra', 'goa', 'karnataka', 'kerala', 'tamil nadu', 'andhra pradesh', 'telangana', 'lakshdweep', 'andaman and nicobar'], 'xcor': [-50.0, -68.0, -90.0, -70.0, -51.0, -41.0, 11.0, 36.0, 92.0, 79.0, 92.0, 90.0, 78.0, 65.0, 58.0, 31.0, 4.0, 10.0, 2.0, -19.0, -53.0, -106.0, -81.0, -70.0, -93.0, -136.0, -89.0, -100.0, -90.0, -77.0, -60.0, -55.0, -55.0, -118.0, 72.0], 'ycor': [137.0, 126.0, 117.0, 98.0, 82.0, 49.0, 31.0, 53.0, 64.0, 36.0, 35.0, 24.0, 7.0, 9.0, 30.0, 5.0, 11.0, 32.0, -18.0, -4.0, 2.0, 41.0, 71.0, 62.0, 87.0, -3.0, -34.0, -75.0, -86.0, -125.0, -119.0, -79.0, -46.0, -126.0, -119.0]}
)
print(df)
#f_csv=df.to_csv("indian_states_and_coordinates."
                # "csv")
print(df.describe())