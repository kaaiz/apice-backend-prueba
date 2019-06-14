from rest_framework import serializers
from .models import Category, Element, Type, Product, User

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'text', 'image', 'created_date',)
        model = Category

class ElementSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'text', 'image', 'category', 'display', 'created_date',)
        model = Element

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'text', 'image', 'created_date',)
        model = Type

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'text', 'image', 'category', 'display', 'price', 'stock', 'created_date',)
        model = Product

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'username', 'first_name', 'last_name', 'is_staff', 'is_active', 'email', 'password', 'created_date',)
        model = User
        
        write_only_fields = ('password',)
        read_only_fields = ('id',)
    
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            is_staff=validated_data['is_staff'],
            is_active=validated_data['is_active'],
            email=validated_data['email'],
            created_date=validated_data['created_date'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user