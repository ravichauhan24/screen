#! C:\screentime\myenv\Scripts\python.exe

import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

data=pd.read_csv("dataset3-1.csv")
# print(data.head())
# print(data.isnull().sum())
# print(data.describe())



# figure=px.bar(data_frame=data,x="ID",y="minority", color="gender", title="Usage Graph By Ravi")
# figure.show(),

# figure=px.scatter(data_frame=data,x="ID",y="Optm",size="gender",trendline="lowess", trendline_options=dict(frac=0.1),color="gender", title="Realtionship between id  and deprived")
# figure.show()

df = px.data.stocks(indexed=True, datetimes=True)
fig = px.scatter(df, trendline="rolling", trendline_options=dict(window=5),
                title="5-point moving average")
fig.data = [t for t in fig.data if t.mode == "lines"]
fig.update_traces(showlegend=True) #trendlines have showlegend=False by default
fig.show()