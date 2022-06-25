from rest_framework.response import Response
from .models import Cart
from .serializers import CartSerializer
from product.models import Product
from rest_framework.views import APIView


class CartView(APIView):
    def get(self, request):
        print("Get in cart")
        cart = Cart.objects.all()
        serializer = CartSerializer(cart, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        print("Post in cart")
        id=request.data
        product=Product.objects.get(id=id)
        cart=Cart.objects.create(product=product)
        cart.save()
        return self.get('GET')