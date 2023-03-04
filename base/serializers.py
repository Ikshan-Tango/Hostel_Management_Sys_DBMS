from rest_framework.serializers import ModelSerializer

from .models import CustomUser,Warden,Caretaker,Student,Room
from rest_framework import serializers


from django.core.exceptions import ValidationError


class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["email","is_student","is_caretaker","is_warden","password"]
        #"__all__"
        exclude = []

    #to make sure that the given mail address is a thapar.edu address
    def validate(self, attrs):

        email = attrs.get("email", None)
        domain = email.split('@')[1]
        domain_list = ["thapar.edu"]
        if domain not in domain_list:
            raise serializers.ValidationError("Please enter your TIET email address.")

        return super().validate(attrs)


class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = ['college_id', 'name', 'age', 'room_num', 'hostel', 'mobile_num', 'branch', 'year','student']
        exclude = []




