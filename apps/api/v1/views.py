from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import UserSerializer, CategorySerializer, CustomerSerializer, RevenueSerializer, ExpenseSerializer
from apps.core.models import User, Category, Customer, Revenue, Expense 
from url_filter.integrations.drf import DjangoFilterBackend


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['name']
class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()

class RevenueViewSet(viewsets.ModelViewSet):
    serializer_class = RevenueSerializer
    queryset = Revenue.objects.all()

class ExpenseViewSet(viewsets.ModelViewSet):
    serializer_class = ExpenseSerializer
    queryset = Expense.objects.all()

