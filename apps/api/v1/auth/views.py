from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomSerializer

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomSerializer
