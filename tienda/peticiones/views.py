from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from peticiones.models import pqrs
from peticiones.serializadores import TutorialSerializer
from rest_framework.decorators import api_view

@api_view(['GET', 'POST', 'DELETE'])
def pqrs_list(request):
    # GET list of peticiones, POST a new pqrs, DELETE all peticiones
    if request.method == 'GET':
        peticiones = pqrs.objects.all()
        
        title = request.GET.get('title', None)
        if title is not None:
            peticiones = peticiones.filter(title__icontains=title)
        
        peticiones_serializer = TutorialSerializer(peticiones, many=True)
        return JsonResponse(peticiones_serializer.data, safe=False)
        # 'safe=False' for objects serialization
    elif request.method == 'POST':
        pqrs_data = JSONParser().parse(request)
        pqrs_serializer = TutorialSerializer(data=pqrs_data)
        if pqrs_serializer.is_valid():
            pqrs_serializer.save()
            return JsonResponse(pqrs_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(pqrs_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        count = pqrs.objects.all().delete()
        return JsonResponse({'message': '{} peticiones were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def pqrs_detail(request, pk):
    # find pqrs by pk (id)
    try: 
        pqr = pqrs.objects.get(pk=pk) 
    except pqr.DoesNotExist: 
        return JsonResponse({'message': 'The pqrs does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    if request.method == 'GET': 
        pqrs_serializer = TutorialSerializer(pqrs) 
        return JsonResponse(pqrs_serializer.data) 
    elif request.method == 'PUT': 
        pqrs_data = JSONParser().parse(request) 
        pqrs_serializer = TutorialSerializer(pqr, data=pqrs_data) 
        if pqrs_serializer.is_valid(): 
            pqrs_serializer.save() 
            return JsonResponse(pqrs_serializer.data) 
        return JsonResponse(pqrs_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    elif request.method == 'DELETE': 
        pqr.delete() 
        return JsonResponse({'message': 'pqrs was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
 
    # GET / PUT / DELETE pqrs
    
        
@api_view(['GET'])
def pqrs_list_published(request):
    peticiones = pqrs.objects.filter(published=True)        
    if request.method == 'GET': 
        peticiones_serializer = TutorialSerializer(peticiones, many=True)
        return JsonResponse(peticiones_serializer.data, safe=False)