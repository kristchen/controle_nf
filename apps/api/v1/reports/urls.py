from apps.api.v1.reports.views import RevenueTotalView, RevenueTotalCustomerView, RevenueTotalMonthView
from django.urls import path

urlpatterns = [
    path('total-revenue/', RevenueTotalView.as_view(), name='total-revenue'),
    path('revenue-by-customer/', RevenueTotalCustomerView.as_view(), name='total-customer'),
    path('revenue-by-month/', RevenueTotalMonthView.as_view(), name='total-month'),
]