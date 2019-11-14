import pandas as pd
import matplotlib.pyplot as plt;
import seaborn as sns;
df = pd.read_csv("attachment_bikeshare.csv")
print(df.head(10))
sns.distplot(df['count']);
plt.savefig('count_hist.png')
print("Skewness %f" %df['count'].skew())
print("Kurtosis %f" %df['count'].kurt())

