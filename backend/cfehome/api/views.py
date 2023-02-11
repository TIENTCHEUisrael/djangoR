#from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
import json
from django.forms.models import model_to_dict
from products.models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.serializers import ProductSerializer


def test(request,*args,**kwargs):
    # request -> HttpRequest -> Django
    # print(dir(request))
    # request.body
    
    print(request.GET) #url query params
    print(request.POST)
    body=request.body #byte string of JSON data
    print(body) #present
    data={}
    try:
        data=json.loads(body) # String of data -> Python Dict
    except:
        pass
    print(data)
    data['params']=dict(request.GET)
    data['headers']=dict(request.headers)
    data['content_type']=request.content_type
    return JsonResponse(data)

@api_view(["GET","POST"])
def test2(request,*args,**kwargs):
    instance=Product.objects.all().order_by("?").first()
    data={}
    if instance:
        #data['title']=model_data.title
        #data['content']=model_data.content
        #data['price']=model_data.price
        #data=model_to_dict(model_data,fields=['id','title','price','sale_price'])
        data=ProductSerializer(instance).data
    return Response(data)

@api_view(['POST'])
def api_home(request,*args,**kwargs):
    """
        DRF API VIEWS
    """
    serializer=ProductSerializer(data=request.data)
    if serializer.is_valid():
        print(serializer.data)
        data=serializer.data
        return Response(data)   