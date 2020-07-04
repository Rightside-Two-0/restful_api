# Generated by Django 3.0.5 on 2020-06-30 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200626_1809'),
    ]

    operations = [
        migrations.AddField(
            model_name='opportunity',
            name='url',
            field=models.CharField(default='', max_length=256),
        ),
        migrations.AlterField(
            model_name='asset',
            name='source',
            field=models.CharField(choices=[('Bitcoin/Crypto', 'Bitcoin/Crypto'), ('Savings', 'Savings'), ('Checking', 'Checking'), ('Bitcoin/Crypto', 'Bitcoin/Crypto'), ('Stocks', 'Stocks'), ('Mutual Funds', 'Mutual Funds'), ('Bank CDs', 'Bank CDs'), ('Real Estate', 'Real Estate'), ('Business', 'Business'), ('Salary/Wages', 'Salary/Wages')], max_length=60),
        ),
        migrations.AlterField(
            model_name='expense',
            name='source',
            field=models.CharField(choices=[('Mortgage/Rent', 'Mortgage/Rent'), ('Utilities', 'Utilities'), ('Insurance', 'Insurance'), ('Food/Groceries', 'Food/Groceries'), ('Vehicle', 'Vehicle'), ('Health/Wellness', 'Health/Wellness'), ('Entertainment', 'Entertainment'), ('Clothing', 'Clothing'), ('Furniture', 'Furniture'), ('Donations/Charity', 'Donations/Charity'), ('Taxes', 'Taxes'), ('Fees/Fines', 'Fees/Fines'), ('Other', 'Other'), ('RE Debt Service', 'RE Debt Service')], max_length=60),
        ),
        migrations.AlterField(
            model_name='ledger',
            name='from_account',
            field=models.CharField(choices=[('Bitcoin/Crypto', 'Bitcoin/Crypto'), ('Checking', 'Checking'), ('Savings', 'Savings'), ('Stocks', 'Stocks'), ('Mutal Funds', 'Mutal Funds'), ('Bank CDs', 'Bank CDs'), ('Real Estate', 'Real Estate'), ('Business', 'Business'), ('Salary/Wages', 'Salary/Wages')], max_length=30),
        ),
        migrations.AlterField(
            model_name='ledger',
            name='to_account',
            field=models.CharField(choices=[('Mortgage/Rent', 'Mortgage/Rent'), ('Utilities', 'Utilities'), ('Insurance', 'Insurance'), ('Food/Groceries', 'Food/Groceries'), ('Vehicle', 'Vehicle'), ('Health/Wellness', 'Health/Wellness'), ('Entertainment', 'Entertainment'), ('Clothing', 'Clothing'), ('Furniture', 'Furniture'), ('Donations/Charity', 'Donations/Charity'), ('Taxes', 'Taxes'), ('Fees/Fines', 'Fees/Fines'), ('Other', 'Other'), ('RE Debt Service', 'RE Debt Service')], max_length=30),
        ),
    ]
