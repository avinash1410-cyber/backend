from django.http import HttpResponse

from product.serializers import ProductSerializer
from .models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
# Create your views here.



class ProductView(APIView):
     def get(self, request, pk=None,format=None):
        if pk:
            print("The required Id is the",pk)
            item = Product.objects.get(id=pk)
            serializer = ProductSerializer(item)
            return Response(serializer.data)
        items = Product.objects.all()
        print("The required Items are ALL")
        serializer = ProductSerializer(items, many=True)
        return Response(serializer.data)