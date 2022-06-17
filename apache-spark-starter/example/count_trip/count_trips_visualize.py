import pandas as pd
import matplotlib.pyplot as plt


trips = pd.read_csv("../../data/result_data/result_trips_data.csv")
trips.plot()
plt.show()
