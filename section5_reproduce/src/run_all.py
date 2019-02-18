import pandas as pd
from analysis_functions import avg_count_birds

sdf = pd.read_csv('../data/birds_lg.csv')
sdf.set_index("Species", inplace=True)
results = avg_count_birds(sdf)
results.to_csv("../results/avg_count_birds_test.csv")
ax = results.T.plot()
fig = ax.get_figure()  # From the axis object, get the whole figure
fig.savefig('../results/birds_results_test.pdf')  # Save the figure

print(results)