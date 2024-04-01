from django.shortcuts import render
from rest_framework.decorators import permission_classes, api_view

from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.permissions import IsAuthenticated

from MarketApp.models import Sellers, Materials
from MarketApp.serializers import SellerSerializer, MaterialSerializer


# Create your views here.
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def material_api(request, id_resp=0):
    if request.method == 'GET':
        if id_resp == 0:
            material_data = Materials.objects.all()
            material_serializer = MaterialSerializer(material_data, many=True).data

            return JsonResponse(material_serializer, safe=False)
        else:
            material_data_by_id = Materials.objects.get(MaterialId=id_resp)
            material_serializer = MaterialSerializer(material_data_by_id, many=False).data

            return JsonResponse(material_serializer, safe=False)

    elif request.method == 'POST':
        material_data = JSONParser().parse(request)
        materials_serializer = MaterialSerializer(data=material_data)
        if materials_serializer.is_valid():
            materials_serializer.save()

            return JsonResponse("Added Successfully", safe=False)

    elif request.method == 'PUT':
        material_data = JSONParser().parse(request)
        material = Materials.objects.get(MaterialId=material_data['MaterialId'])
        materials_serializer = MaterialSerializer(material, data=material_data)
        if materials_serializer.is_valid():
            materials_serializer.save()

            return JsonResponse("Updated Successfully", safe=False)

    elif request.method == 'DELETE':
        material = Materials.objects.get(MaterialId=id_resp)
        material.delete()

        return JsonResponse("Deleted Successfully", safe=False)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def seller_api(request, id_resp=0):
    if request.method == 'GET':
        if id_resp == 0:
            seller_data = Sellers.objects.all()
            seller_serializer = SellerSerializer(seller_data, many=True).data

            return JsonResponse(seller_serializer, safe=False)
        else:
            seller_data_by_id = Sellers.objects.get(SellerId=id_resp)
            seller_serializer = SellerSerializer(seller_data_by_id, many=False).data

            return JsonResponse(seller_serializer, safe=False)

    elif request.method == 'POST':
        seller_data = JSONParser().parse(request)
        sellers_serializer = SellerSerializer(data=seller_data)
        if sellers_serializer.is_valid():
            sellers_serializer.save()

            return JsonResponse("Added Successfully", safe=False)

    elif request.method == 'PUT':
        seller_data = JSONParser().parse(request)
        seller = Sellers.objects.get(SellerId=seller_data['SellerId'])
        sellers_serializer = SellerSerializer(seller, data=seller_data)
        if sellers_serializer.is_valid():
            sellers_serializer.save()

            return JsonResponse("Updated Successfully", safe=False)

    elif request.method == 'DELETE':
        seller = Sellers.objects.get(SellerId=id_resp)
        seller.delete()

        return JsonResponse("Deleted Successfully", safe=False)
