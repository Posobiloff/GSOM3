import seaborn as sns
cars = sns.load_dataset("car_crashes")
cars

import matplotlib.pyplot as plt
plt.figure(figsize = (20, 10))
sns.barplot(data=cars, x='total', y='abbrev', orient='h', width = 2)

plt.figure(figsize = (20, 10))
sns.scatterplot(data=cars, x='speeding', y='alcohol')

plt.figure(figsize = (10, 5))
sns.scatterplot(data=cars, x='total', y='ins_premium')

plt.figure(figsize = (20, 10))
sns.relplot(data=cars, x='alcohol', y='no_previous', hue = "ins_premium")

plt.figure(figsize = (20, 10))
sns.relplot(data=cars, x='ins_premium', y='ins_losses', hue = "not_distracted")

plt.figure(figsize = (20, 10))
sns.barplot(data=cars, x='ins_losses', y='abbrev', orient='h', width = 2)

plt.figure(figsize = (20, 10))
sns.relplot(data=cars, x='not_distracted', y='no_previous', hue = "ins_premium")

plt.figure(figsize = (20, 10))
sns.relplot(data=cars, x='speeding', y='no_previous', hue = "ins_premium")

