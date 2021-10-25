from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.core import serializers

class CustomSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['token'] = str(refresh.access_token)
        user = { 'username': self.user.username,
                 'id':self.user.id,
                 'name':  self.user.name,
                 'email': self.user.email,
                 'cnpj':  self.user.cnpj,
                 'company_name': self.user.company_name,
                 'phone_number': self.user.phone_number}
        data['user'] = user
        return data
