from django.db import models
from django.contrib.auth.models import AbstractUser
from localflavor.br.models import BRCNPJField

class User(AbstractUser):
    name = models.CharField(max_length=255, blank=False)
    email = models.EmailField(max_length=255, blank=False, unique=True)
    cnpj = BRCNPJField(max_length=15, blank=False, unique=True)
    password = models.CharField(max_length=255, blank=False)
    company_name = models.CharField(max_length=255, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)


class Customer(models.Model):
    cnpj = BRCNPJField(max_length=15, blank=False, unique=True)
    comercial_name = models.CharField(max_length=255, blank=False, unique=True)
    legal_name = models.CharField(max_length=255, blank=False, unique=True)
    status = models.BooleanField(null=False, default=True)

class Category(models.Model):
    name = models.CharField(max_length=15, blank=False, unique=True)
    description = models.CharField(max_length=255, blank=False)
    status = models.BooleanField(null=False, default=True)


class Movement(models.Model):
    amount = models.DecimalField(decimal_places=4, max_digits=20, blank=False)
    description = models.CharField(max_length=255, blank=False)
    acctual_date = models.DateField(null=False)
    transcation_date = models.DateField(null=False)
    user = models.ForeignKey(User, related_name='movements', on_delete=models.CASCADE)

class Revenue(Movement):
    invoice_id = models.PositiveIntegerField(null=False)
    customer = models.ForeignKey(Customer, related_name='revenues', on_delete=models.CASCADE)

class Expense(Movement):
    category = models.ForeignKey(Category, related_name='categories',on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)