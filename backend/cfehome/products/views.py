from django.shortcuts import render
from rest_framework import generics
from products.serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
#from django.http import http404
from django.shortcuts import get_list_or_404
from products.models import Product

# Create your views here.

class ProductListApiView(generics.ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    #ici on defini ce qui se passera lors de la creation de l'object product.Comme le fait que si il n'a pas de content il prendra par defaut la valeur de title
    def perform_create(self, serializer):
        #serializer.save(user=self.request.user)
        print(serializer.validated_data)
        title=serializer.validated_data.get('title')
        content=serializer.validated_data.get('content') or None
        if content is None:
            content=title
        serializer.save(content=content)
    
product_List_view=ProductListApiView.as_view()


class ProductDetailApiView(generics.RetrieveAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    
product_detail_view=ProductDetailApiView.as_view()

class ProductCreateApiView(generics.CreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    #ici on defini ce qui se passera lors de la creation de l'object product.Comme le fait que si il n'a pas de content il prendra par defaut la valeur de title
    def perform_create(self, serializer):
        #serializer.save(user=self.request.user)
        print(serializer.validated_data)
        title=serializer.validated_data.get('title')
        content=serializer.validated_data.get('content') or None
        if content is None:
            content=title
        serializer.save(content=content)
    
product_create_view=ProductCreateApiView.as_view()



@api_view(['GET','POST'])
def product_alt_view(request,pk=None,*args,**kwargs):
    method=request.method
    
    if method == "GET":       
        #url_args??
        #get request -> detail view
        if pk is not None:
            #detail view
            obj=get_list_or_404(Product,pk=pk)
            data=ProductSerializer(obj,many=False).data
            return Response(data)
        #list view
        queryset=Product.objects.all()
        data=ProductSerializer(queryset,many=True).data
        return Response(data)
    
    if method=="POST":
        #create item
        serializer=ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):#Retournera l'erreur au niveau de la position ou il se trouvera
            print(serializer.validated_data)
            title=serializer.validated_data.get('title')
            content=serializer.validated_data.get('content') or None
            if content is None:
                content=title
            serializer.save(content=content)
            return Response(data)   
        return Response({"invalid":"not good data"},status=400)