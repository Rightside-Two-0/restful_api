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
    source = models.CharField(max_length=60)
    amount = models.CharField(max_length=30)
    def __str__(self):
        return self.description
    pass

class Expense(models.Model):
    def __str__(self):
        return self.description
    pass

class Asset(models.Model):
    def __str__(self):
        return self.description
    pass

class Liability(models.Model):
    def __str__(self):
        return self.description
    pass

class Opportunity(models.Model):
    def __str__(self):
        return self.description
    pass
