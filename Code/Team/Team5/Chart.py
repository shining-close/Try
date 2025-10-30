import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('company_sales_data.csv')

# Task 1: Plotting Total Profit vs. Month Number
plt.figure(figsize=(10, 5))
plt.plot(data['month_number'], data['total_profit'], label='Profit')

# Adding labels and title
plt.xlabel('Month Number')
plt.ylabel('Total Profit')
plt.title('Company Total Profit per Month')

# Display the plot
plt.grid(True)
plt.show()


# Task 2: Styled Line Plot for Total Profit
plt.figure(figsize=(10, 5))
plt.plot(
    data['month_number'],
    data['total_profit'],
    label='Profit',
    color='red',
    linestyle=':',
    marker='o',
    markerfacecolor='k',
    linewidth=3
)

# Adding labels, title, and legend
plt.xlabel('Month Number')
plt.ylabel('Total Profit')
plt.title('Total Profit with Styling')
plt.legend(loc='lower right')

# Display the plot
plt.grid(True)
plt.show()


# Task 3: Scatter Plot for Toothpaste Sales
plt.figure(figsize=(10, 5))
plt.scatter(data['month_number'], data['toothpaste'], color='blue', label='Toothpaste Sales')

# Adding labels and title
plt.xlabel('Month Number')
plt.ylabel('Number of units sold')
plt.title('Toothpaste Sales per Month')

# Adding grid with a specific style
plt.grid(True, linewidth=1, linestyle='--')

# Adding the legend at the top-left corner
plt.legend(loc='upper left')

# Display the plot
plt.show()

# Task 4
# Example data for task 4 (assuming you have a dictionary of language popularity)
languages = ['Python', 'Java', 'C++', 'Ruby', 'JavaScript', 'R', 'C#']
popularity = [95.5, 45, 40, 35, 90, 60, 78.9]

# Task 4: Horizontal Bar Chart
plt.figure(figsize=(10, 5))
plt.barh(languages, popularity, color=['skyblue','red','green','purple','yellow','cyan','black'])

# Adding labels and title
plt.xlabel('Popularity')
plt.ylabel('Programming Languages')
plt.title('Popularity of Programming Languages')

# -------Turn on the grid-----------These have been commented out to remove the error
plt.minorticks_on()
plt.grid(which='major', linestyle='-',linewidth=0.5, color='red')
plt.grid(which='minor', linestyle=':', linewidth=0.5, color='black')

# Display the plot
plt.show()


# Task 5: pie chart
languages = ['Python', 'Java', 'C++', 'Ruby', 'JavaScript', 'R', 'C#']
popularity = [95.5, 45, 40, 35, 90, 60, 78.9]
color = ['skyblue', 'red', 'green', 'purple', 'yellow', 'cyan', 'black']
explode = (0.2, 0.2, 2, 0.5, 0, 0, 0.5)

# Task 5: Pie Chart
plt.pie(popularity, explode=explode, labels=languages, colors=color,
        autopct='%1.1f%%', shadow=True, startangle=140)

# Display the plot
plt.show()