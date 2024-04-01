from rest_framework import serializers
from MarketApp.models import Sellers, Materials


class MaterialSerializer(serializers.ModelSerializer):

    class Meta:
        model = Materials
        fields = '__all__'


class SellerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sellers
        fields = '__all__'
