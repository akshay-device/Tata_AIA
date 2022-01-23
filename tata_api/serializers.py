from rest_framework import serializers
from .models import tata_rec


class tataRecSer(serializers.ModelSerializer):
    class Meta:
        model = tata_rec
        fields = ('Date_of_Issue', 'Time_of_Issue', 'Form', 'Method','Issue','Caller_ID_Number','Type_of_Call_or_Messge','Advertiser_Business_Number','City','Zip','Location_Center_point_of_the_Zip_Code')

    def create(self, validated_data):
        return tata_rec.objects.create(**validated_data)

    # Field Level Validation
    def validate_Form(self, value):
        lst = ["internet", "accessibility", "tv", "phone", "radio", ]
        if value.lower() not in lst:
            raise serializers.ValidationError("Please Enter Valid Form Input")
        return value

    # Object Level Validation`
    def validate(self, data):
        Met = data.get('Method','')
        Ct = data.get('City','')
        if Met.lower() == 'dsl' and Ct.lower() != 'barry':
            raise serializers.ValidationError("City must be a Barry")
        return data

