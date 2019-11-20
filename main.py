import pandas as pd
import matplotlib.pyplot as plt;
import seaborn as sns;


 

class CsvFile:
  df = None
  def __init__(self,fileName):
    self.fileName=fileName

  def readCsv(self):
    df = pd.read_csv(self.fileName)
    return df
  
  def univariate_Plot(self,df):
    sns.distplot(df['count']);
    print("univariates")
    plt.savefig('count_hist.png') 

  def skew_Kurtosis(self,df):
    print("Skewness %f" % df['count'].skew())#Says about asymmetric behaviour of curve
    print("Kurtosis %f" % df['count'].kurt())

  def bivariate_Plot(self,df):
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


file =CsvFile("attachment_bikeshare.csv")
df = file.readCsv()
#file.univariate_Plot(df)




