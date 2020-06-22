from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from .views import CreateViewIncome, DetailsViewIncome
from .views import CreateViewExpense, DetailsViewExpense
from .views import CreateViewAsset, DetailsViewAsset
from .views import CreateViewLiability, DetailsViewLiability
from .views import CreateViewOpportunity, DetailsViewOpportunity


urlpatterns = [
    path('income/', CreateViewIncome.as_view(), name='new_income'),
    path('income/<int:id>', DetailsViewIncome.as_view(), name='details_income'),
    path('expense/', CreateViewExpense.as_view(), name='new_expense'),
    path('expense/<int:id>', DetailsViewExpense.as_view(), name='details_expense'),
    path('asset/', CreateViewAsset.as_view(), name='new_asset'),
    path('asset/<int:id>', DetailsViewAsset.as_view(), name='details_asset'),
    path('liability/', CreateViewLiability.as_view(), name='new_liability'),
    path('liability/<int:id>', DetailsViewAsset.as_view(), name='details_liability'),
    path('ledger/', CreateViewLedger.as_view(), name='create_view'),
    path('ledger/<int:id>', , name='details_view'),
    path('opportunity/', CreateViewOpportunity.as_view(), name='new_opp'),
    path('opportunity/<int:id>', DetailsViewOpportunity.as_view(), name='details_opp'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
] + urlpatterns
