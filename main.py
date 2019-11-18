import pandas as pd
import matplotlib.pyplot as plt;
import seaborn as sns;
df = pd.read_csv("attachment_bikeshare.csv")
print(df.head(10))
#----------univariate analysis-----------------------
#Histogram/Distribution plot : univariate continous variable => Seaborn lib


sns.distplot(df['count']);
plt.savefig('count_hist.png')
print("Skewness %f" % df['count'].skew())#Says about asymmetric behaviour of curve
print("Kurtosis %f" % df['count'].kurt()) #Thick tailed - more outliers

#-------------bi-variate analysis----------------
#feature engineering
# Barplot  : categorical independent vs continuous dependent output variable (count) => seaborn

#Least rentals in season=1, most rentals in season=3
sns.barplot(x='season',y='count',data=df)
plt.savefig('season_count_bar.png')

#More bike rentals on working day
sns.barplot(x='workingday',y='count',data=df)
plt.savefig('workingday_count_bar.png')

#Slightly more rentals on holidays
sns.barplot(x='holiday',y='count',data=df)
plt.savefig('holiday_count_bar.png')

#Almost same rentals in all weather, sloghtly higher in weather=3
sns.barplot(x='weather',y='count',data=df)
plt.savefig('weather_count_bar.png')

#box plot : Differential calculus(IQR,Mean ..) categorical independent vs continuous dependent output variable (count). Yields same result as bar graph  =>matplotlib.pyplot

var = 'season'
data = pd.concat([df['count'], df[var]], axis=1)
f, ax = plt.subplots(figsize=(8, 6))
fig = sns.boxplot(x=var, y="count", data=data)
fig.axis(ymin=0, ymax=1000);
plt.savefig('season_count_boxplot.png')

# Continuous independent and dependent variable - Scatter plot

#cannot predict correlation from the graph. Looks like temp doesnt depend on the number of bike rentals
var2='temp'
data2=pd.concat([df['count'],df[var2]],axis=1)
data2.plot.scatter(x=var2,y='count',ylim=(0,900))
plt.savefig('temp_count_scatterplot.png')

#Not so great correlation .
var2='casual'
data2=pd.concat([df['count'],df[var2]],axis=1)
data2.plot.scatter(x=var2,y='count',ylim=(0,900))
plt.savefig('casual_count_scatterplot.png')

#Perfect correlation between registered numbers and rentals
var2='registered'
data2=pd.concat([df['count'],df[var2]],axis=1)
data2.plot.scatter(x=var2,y='registered',ylim=(0,900))
plt.savefig('registered_count_scatterplot.png')

#Perfect correlation between hunidity and rentals
var2='humidity'
data2=pd.concat([df['count'],df[var2]],axis=1)
data2.plot.scatter(x=var2,y='humidity',ylim=(0,900))
plt.savefig('humidity_count_scatterplot.png')

#almost Perfect correlation between windspeed numbers and rentals
var2='windspeed'
data2=pd.concat([df['count'],df[var2]],axis=1)
data2.plot.scatter(x=var2,y='windspeed',ylim=(0,900))
plt.savefig('windspeed_count_scatterplot.png')

#Slightly perfect correlation between atemp numbers and rentals
var2='atemp'
data2=pd.concat([df['count'],df[var2]],axis=1)
data2.plot.scatter(x=var2,y='atemp',ylim=(0,900))
plt.savefig('atemp_count_scatterplot.png')

#Find correlation using heatmap
#Features that influence the rental count are - Registeres ,casual,atemp, temp
corrmat = df.corr()
sns.heatmap(corrmat,square=True);
plt.savefig('heatmap.png')














