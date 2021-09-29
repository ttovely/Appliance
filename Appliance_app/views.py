from .models import Category, Appliances
from .serializers import CategorySerializer, AppliancesSerializer, CommentSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly 
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.filters import SearchFilter

class CategoryVievSet(ModelViewSet): 
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated, ]
    filter_backends = [SearchFilter, ]
    search_fields = ['category', ]

    @action(methods=['post', ], detail=True, serializer_class = AppliancesSerializer)
    def add_appliance(self, request, *args, **kwargs):
        category = self.get_object()
        serializer = AppliancesSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            appliance = Appliances.objects.create(
                                            brand=data['brand'],
                                            category=category,
                                            model=data['model'],
                                            price=data['price'],
                                            quantity=data['quantity'],
                                            inStock=data['inStock']
                                        )
            appliance.save()
            serializer = AppliancesSerializer(instance=appliance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

class AppliancesViewSet(ModelViewSet):
    queryset = Appliances.objects.all()
    serializer_class = AppliancesSerializer  
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    filter_backends = [SearchFilter, ]
    search_fields = ['brand', 'category__category', 'model']

    @action(methods=['post',], detail=True, serializer_class = CommentSerializer)
    def add_comment(self, request, *args, **kwargs):
        appliances = self.get_object()
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(author = request.user, appliances = appliances)
            return Response(serializer.data)
                        
    @action(methods=['get', 'post', ], detail=True)
    def minus_quantity(self, request, *args, **kwargs):
        appliances = self.get_object()
        if appliances.quantity > 0:
            appliances.quantity -=1
            if appliances.quantity ==0:
                appliances.inStock = False
                appliances.save()
                serializer = self.get_serializer_class()(instance=appliances)
                return Response(serializer.data)
            else:
                appliances.save()
                appliances = self.get_serializer_class()(instance=appliances)
                return Response(appliances.data)
            
        else:
            return Response({'Error': 'quantity is zero'})

    @action(methods=['get', ], detail=True)
    def add_quantity(self, request, *args, **kwargs):
        appliances = self.get_object()
        appliances.quantity +=1
        appliances.inStock = True
        appliances.save()
        serializer = self.get_serializer_class()(instance=appliances)
        return Response(serializer.data)
