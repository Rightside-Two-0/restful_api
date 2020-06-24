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
    )
    expense_accounts = (
        ('Mortgage/Rent', 'Mortgage/Rent'),
        ('Utilities', 'Utilities'),
        ('Insurances','Insurances'),
        ('Food/Groceries','Food/Groceries'),
        ('Vehicle(s)','Vehicle(s)'),
        ('Health/Wellness','Health/Wellness'),
        ('Entertainment','Entertainment'),
        ('Clothing','Clothing'),
        ('Furniture','Furniture'),
        ('Donations/Charity','Donations/Charity'),
        ('Taxes','Taxes'),
        ('Fees/Fines','Fees/Fines'),
        ('Other','Other'),
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
        ('Insurances','Insurances'),
        ('Food/Groceries','Food/Groceries'),
        ('Vehicle(s)','Vehicle(s)'),
        ('Health/Wellness','Health/Wellness'),
        ('Entertainment','Entertainment'),
        ('Clothing','Clothing'),
        ('Furniture','Furniture'),
        ('Donations/Charity','Donations/Charity'),
        ('Taxes','Taxes'),
        ('Fees/Fines','Fees/Fines'),
        ('Other','Other'),
    )
    source = models.CharField(max_length=60, choices=sources)
    amount = models.CharField(max_length=30)
    def __str__(self):
        return 'Working on this one...'
class Asset(models.Model):
    sources = (
        ('Savings','Savings'),
        ('Checking','Checking'),
        ('Bitcoin/Crypto','Bitcoin/Crypto'),
        ('Stocks','Stocks'),
        ('Mutual Funds','Mutual Funds'),
        ('Bank CDs','Bank CDs'),
        ('Real Estate','Real Estate'),
        ('Business','Business'),#~~~mind~~your~~own~~business~~
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
    heading = models.CharField(max_length=30)
    description = models.CharField(max_length=256)
    cost = models.CharField(max_length=30)
    down = models.CharField(max_length=30)
    mortgage = models.CharField(max_length=30)
    cash_flow = models.CharField(max_length=30)
    def __str__(self):
        return self.description
