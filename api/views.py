from rest_framework import generics
from .serializers import LedgerSerializer, IncomeSerializer, ExpenseSerializer, AssetSerializer, LiabilitySerializer, OpportunitySerializer
from .models import Ledger, Income, Expense, Asset, Liability, Opportunity

class CreateViewIncome(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()

class DetailsViewIncome(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer

class CreateViewExpense(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()

class DetailsViewExpense(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

class CreateViewAsset(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()

class DetailsViewAsset(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer

class CreateViewLiability(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Liability.objects.all()
    serializer_class = LiabilitySerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()

class DetailsViewLiability(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = Liability.objects.all()
    serializer_class = LiabilitySerializer

class CreateViewOpportunity(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Opportunity.objects.all()
    serializer_class = OpportunitySerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()

class DetailsViewOpportunity(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = Opportunity.objects.all()
    serializer_class = OpportunitySerializer

class CreateViewLedger(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Ledger.objects.all()
    serializer_class = LedgerSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()

class DetailsViewLedger(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = Ledger.objects.all()
    serializer_class = LedgerSerializer
#~~~~~~~~~~~~~~~~~~^^^done^^~~~~~~~~~~~~~~~~~~~~~~~~
