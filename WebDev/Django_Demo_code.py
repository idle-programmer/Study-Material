# model.py 
# from django.db import models

# class Product(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=100, null=False)
#     class Meta:
#     db_table = "product"

# serializer.py
# from rest_framework import serializers
# class productSerializer(serializers.ModelSeralizer):
#     class Meta:
#     model = Product
#     fields = "__all__"

# views.py
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from .model import Product

# class ProductView(APIView):
#     def get(self,request):
#         try: 
#             products = Product.objects.all()
#             serializer = productSerializer(products, many = True)
#             return Response(serializer.data, status=200)
#         except Exception as e:
#             return Response ({"error":str(e)}, status = 500)

#     def post(self, request):
#         try:
#             data = request.data
#             serialiser = productSerializer(data = data)
#             if serialiser.is_valid():
#                 serializer.save()
#                 return Response({"msg":"Product stored successfully"}status=201)
#             return Response({"msg":"Product stored failed"}status=400)
#         except Exception as e:
#             return Response ({"error":str(e)}, status = 500)

# urls.py
# from django.urls import path
# from .views import ProductView

# url_patterns = [
# path("/", ProductView.as_view())
# ]