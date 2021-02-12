from rest_framework import serializers
from .models import *


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = '__all__'


class SocialNetworkSerializer(serializers.ModelSerializer):
    partner = PartnerSerializer()
    category = CategorySerializers()

    class Meta:
        model = SocialNetwork
        fields = '__all__'