# This entrypoint file to be used in development. Start by reading README.md
###import time_series_visualizer
###from unittest import main

# Test your function by calling it here
###time_series_visualizer.draw_line_plot()
###time_series_visualizer.draw_bar_plot()
###time_series_visualizer.draw_box_plot()

# Run unit tests automatically
###main(module='test_module', exit=False)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

df = pd.read_csv('fcc-forum-pageviews.csv',index_col = 'date')
df = df.loc[(df['value'] >= df['value'].quantile(0.025)) &
                (df['value'] <= df['value'].quantile(0.975))]
print(df.index.month().unique())