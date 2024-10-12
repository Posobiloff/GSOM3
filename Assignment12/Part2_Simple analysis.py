import numpy as np
income = np.array([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000], dtype = int)
income
income_without_tax = income * 0.7
income_without_tax
expenses = np.array([500, 1000, 1000, 2000, 2000, 3000, 3000, 4000, 3000, 2000], dtype = int)
expenses
import pandas as pd
d = {
    "Expenses (mln. $)": pd.Series(expenses, ["Jan.", "Feb.", "Mar.", "Apr.", "May", "Jun.", "Jul.", "Aug.", "Sep.", "Oct."]),
    "Income without tax (mln. $)": pd.Series(income_without_tax, ["Jan.", "Feb.", "Mar.", "Apr.", "May", "Jun.", "Jul.", "Aug.", "Sep.", "Oct."])
}
annual_report = pd.DataFrame(d)
annual_report
annual_report.iloc[:3]