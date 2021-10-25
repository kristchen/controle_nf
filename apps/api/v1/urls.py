from rest_framework.routers import DefaultRouter
from .views import UserViewSet, CategoryViewSet, CustomerViewSet, RevenueViewSet, ExpenseViewSet
from apps.api.v1.auth.views import CustomTokenObtainPairView
from django.urls import path, include



router = DefaultRouter()

router.register('users', UserViewSet)
router.register('categories', CategoryViewSet)
router.register('customers', CustomerViewSet)
router.register('revenues', RevenueViewSet)
router.register('expenses', ExpenseViewSet)


urlpatterns = router.urls
urlpatterns += [
    path('auth/', CustomTokenObtainPairView.as_view(), name='auth'),
    path('reports/', include(('apps.api.v1.reports.urls'))),
]

