import streamlit as st
import datetime

st.title("Cash Flow App")

date = st.sidebar.date_input('Date', datetime.date(2020,1,1))
main_cat = st.sidebar.selectbox('Main Categories',
                        ('Incomes', 'Investments', 'Expenses', 'Liabilities', 'Savings'))

if main_cat == 'Expenses':
    subcat = st.sidebar.selectbox('Expenses',
                                ('Food', 'Transportation', 'Health', 'Insurance',
                                'Charities', 'Entertainment', 'Other'))
    if subcat == 'Food':
        detailed_cat = st.sidebar.selectbox('Fastfood','Restaurants','Drinks')
    elif subcat == 'Transportation':
        detailed_cat = st.sidebar.selectbox('Toyota 2014 Payment', 'Toyota 2019 Payment', '' )
elif main_cat == 'Liabilities':
    subcat = st.sidebar.selectbox('Liabilities',
                                  ('Student Loan', 'Credit Card', 'Mortgage Loan', 'Auto Loan'))
elif main_cat == 'Savings':
    subcat = st.sidebar.selectbox('Savings',
                                  ('Emergency', 'Retirement', 'Maintanance', 'Vacation', 'Wedding', 'Mortgage'))
elif main_cat == 'Incomes':
    subcat = st.sidebar.selectbox('Incomes',
                                  ('Work', 'Stock'))
elif main_cat == 'Investments':
    subcat = st.sidebar.selectbox('Investments',
                                  ('Stock'))



def add_cash_flow(date, main_cat, sub_cat):






# self.cash_flow_cols = ['Date', 'Categories', 'Subcategories', 'DetailedCat'
#                                 'Description', 'Note', 'Amount', 'Balance']
#         # # # Categories # # #
#         self.main_cats = ['Expense', 'Saving', 'Income', 'Investment']

#         # expenses
#         self.expense_cats = ['Food', 'Transportation', 'Health', 'Insurance', 'Charities', 'Entertainment', 'Other']

#         # liabilities:
#         self.liability_cats = ['Student Loan', 'Credit Card', 'Mortgage Loan', 'Auto Loan']

#         # savings
#         self.saving_cats = ['Emergency', 'Retirement', 'Maintanance', 'Vacation', 'Wedding', 'Mortgage']

#         # income
#         self.income_cats = ['Engineering', 'Stock']

#         # investment
#         self.investment_cats = ['Stock']

