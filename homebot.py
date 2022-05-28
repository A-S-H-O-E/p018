import pandas as pd 
import plotly.figure_factory as pff
df = pd.read_csv('dataa.csv')
rate = df['Avg Rating'].tolist()
graph = pff.create_distplot([rate],['average rating'],show_hist=  False)
graph.show()