import pandas as pd
import plotly.express as px

df=pd.read_csv("Covid19Chart.csv")
fig=px.line(x="date",y="cases",color="country")
fig.show()