from rest_framework import generics
from rest_framework.response import Response
from apps.core.models import Revenue
from django.db.models import Max, Sum, DecimalField, F
from django.db.models.functions import Coalesce
import calendar

class RevenueTotalView(generics.ListCreateAPIView):

    queryset = Revenue.objects.all()

    def post(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        fields = queryset.filter(transcation_date__year=request.data['fiscal_year']).aggregate(total_revenue=Coalesce(Sum('amount'), 0, output_field=DecimalField()), max_revenue_amount=Coalesce(Max('amount'), 0, output_field=DecimalField()))
        sclass = self.get_serializer_class()
        return Response(sclass(fields).data)


class RevenueTotalMonthView(generics.ListCreateAPIView):

    queryset = Revenue.objects.all()

    def post(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        months = queryset.filter(acctual_date__year=request.data['fiscal_year']).values('transcation_date__month').annotate(total_revenue=Sum('amount'))
        months_list = list(months)
        for d in months_list:
            d.update((k,  calendar.month_name[v]) for k, v in d.items() if v < 13 and v > 0 )
        max_revenue_amount = sum([mont['total_revenue'] for mont in months_list])
        return Response({'months':months_list, 'max_revenue_amount': max_revenue_amount})


class RevenueTotalCustomerView(generics.ListCreateAPIView):

    queryset = Revenue.objects.all()

    def post(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        customers = queryset.filter(acctual_date__year=request.data['fiscal_year']).values(name=F('customer__comercial_name')).annotate(total_revenue=Sum('amount'))
        customer_list = list(customers)
        max_revenue_amount = sum([cust['total_revenue'] for cust in customer_list])
        return Response({'customers':customer_list, 'max_revenue_amount': max_revenue_amount})