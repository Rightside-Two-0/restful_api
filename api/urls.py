from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from .views import CreateViewIncome, DetailsViewIncome
from .views import CreateViewExpense, DetailsViewExpense
from .views import CreateViewAsset, DetailsViewAsset
from .views import CreateViewLiability, DetailsViewLiability
from .views import CreateViewOpportunity, DetailsViewOpportunity
from .views import CreateViewLedger, DetailsViewLedger

urlpatterns = [
    path('income/', CreateViewIncome.as_view(), name='new_income'),
    path('income/<int:pk>', DetailsViewIncome.as_view(), name='details_income'),
    path('expense/', CreateViewExpense.as_view(), name='new_expense'),
    path('expense/<int:pk>', DetailsViewExpense.as_view(), name='details_expense'),
    path('asset/', CreateViewAsset.as_view(), name='new_asset'),
    path('asset/<int:pk>', DetailsViewAsset.as_view(), name='details_asset'),
    path('liability/', CreateViewLiability.as_view(), name='new_liability'),
    path('liability/<int:pk>', DetailsViewLiability.as_view(), name='details_liability'),
    path('ledger/', CreateViewLedger.as_view(), name='create_view'),
    path('ledger/<int:pk>', DetailsViewLedger.as_view(), name='details_view'),
    path('opportunity/', CreateViewOpportunity.as_view(), name='new_opp'),
    path('opportunity/<int:pk>', DetailsViewOpportunity.as_view(), name='details_opp'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
] + urlpatterns
