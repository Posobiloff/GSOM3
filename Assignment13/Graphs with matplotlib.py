import numpy as np
income = np.array([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000], dtype = int)
income_without_tax = income * 0.7
expenses = np.array([500, 1000, 1000, 2000, 2000, 3000, 3000, 4000, 3000, 2000], dtype = int)
import pandas as pd
d = {
    "Expenses (mln. $)": pd.Series(expenses, ["Jan.", "Feb.", "Mar.", "Apr.", "May", "Jun.", "Jul.", "Aug.", "Sep.", "Oct."]),
    "Income without tax (mln. $)": pd.Series(income_without_tax, ["Jan.", "Feb.", "Mar.", "Apr.", "May", "Jun.", "Jul.", "Aug.", "Sep.", "Oct."])
}
annual_report = pd.DataFrame(d)
annual_report


import matplotlib.pyplot as plt
xpoints = ["Jan.", "Feb.", "Mar.", "Apr.", "May", "Jun.", "Jul.", "Aug.", "Sep.", "Oct."]
#bar 1
plt.subplot(1,2,1)
plt.plot(xpoints, income, color = "r")
plt.title("INCOME")

#bar 2
plt.subplot(1,2,2)
plt.plot(xpoints, income_without_tax, color = "b")
plt.title("INCOME WITHOUT TAX")

#bar 3
plt.subplot(1,2,1)
plt.bar(xpoints, income-expenses, color = "m")
plt.title("SAVINGS")
#bar 3
plt.subplot(1,2,2)
plt.bar(xpoints, income_without_tax-expenses, color = "cyan")
plt.title("NET SAVINGS")

general_savings = sum(income_without_tax-expenses)
savings = income_without_tax-expenses
shares = savings/general_savings
plt.pie(shares, labels = xpoints, autopct='%1.1f%%', colors=['r', 'g', 'b', 'c', 'm', 'y', 'maroon', 'w','rosybrown', 'gray'] )


import statistics as st
print(f"The average income for the first quarter is {st.mean([income_without_tax[0], income_without_tax[1], income_without_tax[2]])} $")
print(f"The average income for the second quarter is {st.mean([income_without_tax[3], income_without_tax[4], income_without_tax[5]])} $")
print(f"The average income for the third quarter is {st.mean([income_without_tax[6], income_without_tax[7], income_without_tax[8]])} $")