from . import Expense
import matplotlib.pyplot as plt
class BudgetList():
    def __init__(self, budget):
        self.budget = budget
        self.sum_expenses = 0
        self.expenses = []
        self.sum_overages = 0
        self.overages = []

    def append(self,item):
         # add items to expenses that are under budget
         
        if((self.sum_expenses+item)< self.budget):
            self.expenses.append(item)
            self.sum_expenses+=item
        #add items to overages that are over budget
        else:
            self.overages.append(item)
            self.sum_overages+=item
        
    def __len__(self):
       return (len(self.expenses) + len(self.overages))
        
    def __iter__(self):
     self.iter_e = iter(self.expenses)
     self.iter_o = iter(self.overages)
     return self 

    def __next__(self):
        try:
            return next(self.iter_e)
        except StopIteration as stop:
            return next(self.iter_o)

def main():
    myBudgetList = BudgetList(1200)
    expenses = Expense.Expenses()
    expenses.read_expenses('data/spending_data.csv')
    for expense in expenses.list:
        myBudgetList.append(expense.amount)
        print('The count of all expenses: '+ str(len(myBudgetList)))
    for entry in myBudgetList:
        print(entry)
    # create figure and axis
    (fig, ax) = plt.subplots()
    labels = ['Expenses', 'Overages', 'Budget']
    values = [myBudgetList.sum_expenses, myBudgetList.sum_overages,myBudgetList.budget]
    #create barchart
    ax.bar(labels,values,color=['green', 'red', 'blue'])
    ax.set_title('Your total expenses vs your total budget')
    plt.show()
if (__name__ == '__main__'):
     main()



      
        