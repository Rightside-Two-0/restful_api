from django.db import models

# Create your models here.
class Ledger(models.Model):
    date = models.DateField()
    credit_accounts = (
        ('Bitcoin/Crypto','Bitcoin/Crypto'),
        ('Checking','Checking'),
        ('Savings','Savings'),
        ('Stocks','Stocks'),
        ('Mutal Funds','Mutal Funds'),
        ('Bank CDs','Bank CDs'),
        ('Real Estate','Real Estate'),
        ('Business','Business'),
        ('Salary/Wages','Salary/Wages'),
    )
    expense_accounts = (
        ('Mortgage/Rent', 'Mortgage/Rent'),
        ('Utilities', 'Utilities'),
        ('Insurance','Insurance'),
        ('Food/Groceries','Food/Groceries'),
        ('Vehicle','Vehicle'),
        ('Health/Wellness','Health/Wellness'),
        ('Entertainment','Entertainment'),
        ('Clothing','Clothing'),
        ('Furniture','Furniture'),
        ('Donations/Charity','Donations/Charity'),
        ('Taxes','Taxes'),
        ('Fees/Fines','Fees/Fines'),
        ('Other','Other'),
        ('RE Debt Service','RE Debt Service'),
    )
    from_account = models.CharField(max_length=30, choices=credit_accounts)
    to_account = models.CharField(max_length=30, choices=expense_accounts)
    amount = models.CharField(max_length=20)
    notes = models.CharField(max_length=100)

    def __str__(self):
        return self.notes
class Income(models.Model):
    sources = (
        ('Salary/Wages','Salary/Wages'),
        ('Interest','Interest'),
        ('Dividends','Dividends'),
        ('Real Estate','Real Estate'),
        ('Business','Business'),
    )
    source = models.CharField(max_length=60, choices=sources)
    amount = models.CharField(max_length=30)
    notes = models.CharField(max_length=100)
    def __str__(self):
        return self.notes
class Expense(models.Model):
    sources = (
        ('Mortgage/Rent', 'Mortgage/Rent'),
        ('Utilities', 'Utilities'),
        ('Insurance','Insurance'),
        ('Food/Groceries','Food/Groceries'),
        ('Vehicle','Vehicle'),
        ('Health/Wellness','Health/Wellness'),
        ('Entertainment','Entertainment'),
        ('Clothing','Clothing'),
        ('Furniture','Furniture'),
        ('Donations/Charity','Donations/Charity'),
        ('Taxes','Taxes'),
        ('Fees/Fines','Fees/Fines'),
        ('Other','Other'),
        ('RE Debt Service','RE Debt Service'),
    )
    source = models.CharField(max_length=60, choices=sources)
    amount = models.CharField(max_length=30)
    def __str__(self):
        return self.source
class Asset(models.Model):
    sources = (
        ('Bitcoin/Crypto','Bitcoin/Crypto'),
        ('Savings','Savings'),
        ('Checking','Checking'),
        ('Bitcoin/Crypto','Bitcoin/Crypto'),
        ('Stocks','Stocks'),
        ('Mutual Funds','Mutual Funds'),
        ('Bank CDs','Bank CDs'),
        ('Real Estate','Real Estate'),
        ('Business','Business'),#~~~mind~~your~~own~~business~~
        ('Salary/Wages','Salary/Wages'),
    )
    source = models.CharField(max_length=60, choices=sources)
    down = models.CharField(max_length=30)
    cost = models.CharField(max_length=30)
    notes = models.CharField(max_length=100)
    def __str__(self):
        return self.notes
class Liability(models.Model):
    sources = (
        ('Home Mortgage','Home Mortgage'),
        ('School Loans','School Loans'),
        ('Car Loans','Car Loans'),
        ('Credit Cards','Credit Cards'),
        ('Retaill Debt','Retail Debt'),
        ('RE Mortgages','RE Mortgages'),
        ('Business Debts','Business Debts'),
        ('Bank Loans','Bank Loans'),
    )
    source = models.CharField(max_length=60, choices=sources)
    amount = models.CharField(max_length=30)
    notes = models.CharField(max_length=100)
    def __str__(self):
        return self.notes
class Opportunity(models.Model):
    heading = models.CharField(max_length=30, default='')
    description = models.CharField(max_length=256, default='')
    url = models.CharField(max_length=256, default='')
    cost = models.CharField(max_length=30, default='')
    down = models.CharField(max_length=30, default='')
    mortgage = models.CharField(max_length=30, default='')
    cash_flow = models.CharField(max_length=30, default='')
    coc = models.CharField(max_length=13, default='')
    irr = models.CharField(max_length=13, default='')
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
    #~~~~~~~incomes~~~~~~~~~~~~~~~~~~~~~~~~>
    ask = models.CharField(max_length=30, default='')
    sqft = models.CharField(max_length=30, default='')
    units = models.CharField(max_length=30, default='')
    ave_rent = models.CharField(max_length=30, default='')
    vacancy_rate = models.CharField(max_length=30, default='')
    other_income = models.CharField(max_length=30, default='')
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
    #~~~~~~~expenses~~~~~~~~~~~~~~~~~~~~~~~~>
    repairs = models.CharField(max_length=30, default='')
    management = models.CharField(max_length=30, default='')
    taxes = models.CharField(max_length=30, default='')
    insurance = models.CharField(max_length=30, default='')
    wages = models.CharField(max_length=30, default='')
    utilities = models.CharField(max_length=30, default='')
    gen_admin = models.CharField(max_length=30, default='')
    professional_fees = models.CharField(max_length=30, default='')
    advertising = models.CharField(max_length=30, default='')
    cap_x = models.CharField(max_length=30, default='')
    other = models.CharField(max_length=30, default='')
    def __str__(self):
        return self.description
