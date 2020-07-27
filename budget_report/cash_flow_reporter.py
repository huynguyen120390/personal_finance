import pandas as pd
class CashFlowReporter:
    def __init__(self):
        self.cash_flow_cols = ['Date', 'Categories', 'Subcategories', 'DetailedCat'
                                'Description', 'Note', 'Amount', 'Balance']
        # # # Categories # # #
        self.main_cats = ['Expense', 'Saving', 'Income', 'Investment']

        # expenses
        self.expense_cats = ['Food', 'Transportation', 'Health', 'Insurance', 'Charities', 'Entertainment', 'Other']

        # liabilities:
        self.liability_cats = ['Student Loan', 'Credit Card', 'Mortgage Loan', 'Auto Loan']

        # savings
        self.saving_cats = ['Emergency', 'Retirement', 'Maintenance', 'Vacation', 'Wedding', 'Mortgage']

        # income
        self.income_cats = ['Engineering', 'Stock']

        # investment
        self.investment_cats = ['Stock']

        # # # Budget Dict # # #
        self.budgets = {}

        self.budget_df = pd.DataFrame(columns=self.cash_flow_cols)

    def create_empty_budget_dict(self):
        for main_cat in self.main_cats:
            self.budgets[main_cat] = {}
        for exp in self.expense_cats:
            self.budgets['Expense'][exp] = None
        for sav in self.saving_cats:
            self.budgets['Saving'][sav] = None
        for inc in self.income_cats:
            self.budgets['Income'][inc] = None
        for inv in self.investment_cats:
            self.budgets['Investment'][inv] = None 
    
    def add_cash_flow(self, transaction):
        pass


   

        
        



if __name__ == '__main__':
    cashflow = CashFlowReporter()
    cashflow.create_empty_budget_dict()