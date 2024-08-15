import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("-"*25,"\nGowtham Karthikeyan S\n21BBS0157\nQuestion 2\n","-"*25)

df = pd.read_csv(r'..\diesel_p.csv')
print(df.head(2))

print("Line Chart")
df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')
plt.figure(figsize=(8, 6))
plt.plot(df['Date'], df['Rate'], label='Diesel')
plt.title('Diesel fuel price history (2002-2020)')
plt.xlabel('Year')
plt.ylabel('Price')
plt.legend(loc="upper left")
plt.grid(True)
plt.show()


print("\nHeat map: ")
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month_name()
dp = df.pivot_table(values='Rate', index='Year', columns='Month', aggfunc='mean')
fig, (ax1) = plt.subplots(1, 1, figsize=(15, 15))
sns.heatmap(dp, ax=ax1, cmap='YlOrRd', annot=True, fmt='.2f')
ax1.set_title('Average Diesel Prices by Month and Year')
plt.tight_layout()
plt.show()


print("\nScatter Plot")
plt.figure(figsize=(6, 6))
sns.scatterplot(data=df, x='Rate', y='Date')
plt.title('Correlation between Diesel Prices and Date(2002-2020)')
plt.xlabel('Price')
plt.ylabel('Date')
plt.show()


print('\nHistogram:')
plt.figure(figsize=(6, 6))
sns.histplot(data=df.melt(id_vars='Date', value_vars=['Rate'], var_name='Fuel Type', value_name='Price'), x='Price', hue='Fuel Type', kde=True, bins=30)
plt.title('Distribution of Diesel Prices (2002-2020)')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.show()