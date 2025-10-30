import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Code\Example\Pandas\shopping.csv', parse_dates=['Date'], dayfirst=True)

df.fillna({'Product': 'Unknown', 'Quantity': 0, 'Price': 0.0, 'Total': 0.0}, inplace=True)

df['Total'] = df['Quantity'] * df['Price']

product_sales = df.groupby('Product')['Quantity'].sum()
product_sales.plot(kind='bar')
plt.show()

df['Month'] = df['Date'].dt.to_period('M')
monthly_sales = df.groupby('Month')['Total'].sum()
monthly_sales.plot(kind='line')
plt.show()