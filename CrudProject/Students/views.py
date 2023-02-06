from rest_framework.decorators import api_view
from .serializers import StudentSerializer, StudentModel
from rest_framework.response import Response
from rest_framework.views import APIView



@api_view(['GET', 'POST'])
def add_student_api(request):
    if request.method == 'GET':
        fetched_data = StudentModel.objects.all()   #Python
        des_serializer = StudentSerializer(fetched_data, many=True) #Python to json
        return Response(data=des_serializer.data)
    elif request.method == 'POST':
        data_to_insert = request.data                           #json
        serializer = StudentSerializer(data=data_to_insert)     #Python
        if serializer.is_valid():                               # will call create method from serializer
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors)


@api_view(['PUT', 'GET', 'DELETE', 'PATCH'])
def student_particular(request, pk=None):
    fetch_particular = StudentModel.objects.get(pk=pk)
    de_serializer = StudentSerializer(fetch_particular)
    if request.method == 'PUT':
        serializer = StudentSerializer(data=request.data, instance=fetch_particular, partial=True)
        if serializer.is_valid():                               # will call update method from serializer
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    elif request.method == 'DELETE':
        data_to_be_deleted = StudentModel.objects.get(pk=pk)
        data_to_be_deleted.delete()
        return Response(data={'detail': 'deleted successfully !!!'})

    elif request.method == 'PATCH':
        data = request.data
        serializer = StudentSerializer(data=data, instance=fetch_particular, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
    
    return Response(data=de_serializer.data)

"""-------------------------------------------------------------------------------------------------------------------------"""









