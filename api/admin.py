from django.contrib import admin
from .models import Income, Expense, Liability, Ledger, Asset, Opportunity
# Register your models here.
admin.site.register(Income)
admin.site.register(Expense)
admin.site.register(Liability)
admin.site.register(Ledger)
admin.site.register(Asset)
admin.site.register(Opportunity)
