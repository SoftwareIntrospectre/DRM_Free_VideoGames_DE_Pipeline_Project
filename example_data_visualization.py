import matplotlib.pyplot as plt

# Example Data
categories = ['DRM-Free', 'DRM-Protected']
sales = [300, 700]  # Example sales data, you should replace it with your actual data

# Plotting the data
plt.figure(figsize=(8, 6))
plt.bar(categories, sales, color=['green', 'red'])
plt.title('Sales Distribution of DRM-Free vs DRM-Protected Video Games')
plt.xlabel('DRM Type')
plt.ylabel('Number of Sales (in millions)')

# Adding Data Labels
for i, value in enumerate(sales):
    plt.text(i, value + 10, str(value), ha='center', va='bottom')

# Display the plot
plt.show()
