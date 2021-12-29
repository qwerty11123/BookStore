from rest_framework import serializers
from django import forms
from .models import *
from django.contrib.auth.models import User

from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class RegisterUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True, required=True,validators=[validate_password])
    #confirm_password = serializers.CharField(write_only=True,required=True)

    class Meta:
        model = User
        fields = ['username','password','first_name','last_name','email']

    #def validate(self, attrs):
    #    if attrs['password'] != attrs['confirm_password']:
    #        raise serializers.ValidationError({"password":"password fields didn't match"})
    #    return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],

            )
        user.set_password(validated_data['password'])
        user.save()
        return user









