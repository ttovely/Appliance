from django.db.models import fields 
from rest_framework.serializers import ModelSerializer
from .models import Category, Appliances, Comment

class CommentSerializer(ModelSerializer):
    class Meta:
        model=Comment
        fields = ['id', 'author', 'appliances', 'text', 'posted_at']
        read_only_fields = ['author', 'appliances', 'posted_at']

class AppliancesSerializer(ModelSerializer):
    comment_appliance= CommentSerializer(many=True, read_only=True)
    class Meta:
        model=Appliances
        fields = ['id', 'category', 'brand', 'model', 'price', 'quantity', 'inStock', 'comment_appliance']
        read_only_fields = ['category', 'inStock']

class CategorySerializer(ModelSerializer):
    appliances = AppliancesSerializer(many=True, read_only=True)
    class Meta:
        model=Category
        fields = ['id', 'category', 'appliances']

