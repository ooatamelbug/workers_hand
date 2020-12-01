from .models import Category, City, Workers, Home, RateWorkers, Phone, Governorate
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '_all_'


class GovernorateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Governorate
        fields = '_all_'


class CitySerializer(serializers.ModelSerializer):
    governorate = GovernorateSerializer()

    class Meta:
        model = City
        fields = ['name', 'governorate', 'date_created', 'date_modified']


class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = '_all_'


class WorkersSerializer(serializers.ModelSerializer):
    phones = PhoneSerializer(source='phones_set', many=True)
    rates = PhoneSerializer(source='rates_set', many=True)
    governorate = GovernorateSerializer()
    city = CitySerializer()
    category = CategorySerializer()

    class Meta:
        model = Workers
        fields = [
            'name', 'address', 'governorate', 'city',
            'desc', 'rate', 'total_rate', 'work_time', 'category'
            'phones', 'rates', 'date_created', 'date_modified'
        ]


class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = '_all_'


class RateWorkersSerializer(serializers.ModelSerializer):
    class Meta:
        model = RateWorkers
        fields = '_all_'
