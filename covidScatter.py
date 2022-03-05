import pandas as pd
import plotly.express as px

df = pd.read_csv("C103/PRO-C103/Copy+of+data+-+data.csv")
fig = px.scatter(df,x = "date", y = "cases", color = "country")
fig.show()