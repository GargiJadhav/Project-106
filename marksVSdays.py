import pandas as pd
import plotly.express as pe
import numpy as np


data = pd.read_csv("marksVSdays.csv")

marks = data["Marks In Percentage"].tolist()

days = data["Days Present"].tolist()

graph = pe.scatter(data , x = "Days Present" , y = "Marks In Percentage")
graph.show()

correlation = np.corrcoef(marks , days)

print("Correlation is " , correlation[0,1])



