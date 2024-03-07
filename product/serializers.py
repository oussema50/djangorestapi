from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta: #the class Meta help you  to send all the fields or some fields  to the views 
        model = Product
        fields = "__all__" # or ('name','price','stocke') choise the fields that you want to show in the wiews