import matplotlib.pyplot as plt
from . import Expense
import collections


#read in the spending data

expenses = Expense.Expenses()
expenses.read_expenses('data/spending_data.csv')

#create empty list of spending categories 

spending_categories = []

for expense in expenses.list:
    spending_categories.append(expense.category)

spending_counter = collections.Counter(spending_categories)



# get the top 5 categories 
top5 = spending_counter.most_common(5)
#convert top 5 dictionary to two lists
(categories, count)= zip(*top5)
# plot the top 5 most common categories
fig,ax =plt.subplots()
#bar chart
ax.bar(categories, count)
ax.set_title('# of Purchases by Category')
plt.show()
