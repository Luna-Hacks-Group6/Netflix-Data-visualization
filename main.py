

df = pd.read_csv('C:\Users\user\Desktop\LUNA HACKS 1.0\NetflixDataVisualisastion\netflix_titles.csv')
print(df.head())

for i in df.columns:
  null_rate = df[i].isna().sum() / len(df) * 100
  if null_rate > 0:
    print("{} null rate: {}%".format(i, round(null_rate, 2)))
j
#dealing with missing data
df['country'] = df['country'].fillna(df['country'].mode()[0])
df['cast'].replace(np.nan, 'No data', inplace=True)
df['director'].replace(np.nan, 'No data', inplace=True)
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

df['date_added'] = pd.to_datetime(df['date_added'])
df['month_added'] = df['date_added'].dt.month
df['month_name_added'] = df['date_added'].dt.month_name()
df['year_added'] = df['date_added'].dt.year

sns.palplot(['#221f1f', '#b20710', '#e50914', '#f5f5f1'])
plt.title("Netflix brand palette",
          loc='left',
          fontfamily='serif',
          fontsize=15,
          y=1.2)
plt.show()

x = df.groupby(['type'])['type'].count()
y = len(df)
r=((x/y)).round(2)
mf_ratio = pd.DataFrame(r).T