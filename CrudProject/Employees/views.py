from rest_framework import viewsets
from .serializers import EmployeeSerializer, EmployeeModel
from rest_framework.response import Response


class EmployeeCreateViewSet(viewsets.ViewSet):
    serializer_class = EmployeeSerializer

    def create(self, request):
        data_recieved = request.data
        serializer = self.serializer_class(data=data_recieved)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors)

    def list(self, request):
        data_fetched = EmployeeModel.objects.all()
        de_serializer = self.serializer_class(data_fetched, many=True)
        return Response(data=de_serializer.data)

    def retrieve(self, request, pk=None):
        particular_data = EmployeeModel.objects.get(pk=pk)
        de_serializer = self.serializer_class(particular_data)
        return Response(data=de_serializer.data)
    
    def update(self, request, pk=None):
        data_recieved = request.data
        data_fetched = EmployeeModel.objects.get(pk=pk)
        serializer = self.serializer_class(data=data_recieved, instance=data_fetched)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors)

    def partial_update(self, request, pk=None):
        data_recieved = request.data
        data_fetched = EmployeeModel.objects.get(pk=pk)
        serializer = self.serializer_class(data=data_recieved, instance=data_fetched, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors)

    def destroy(self, request, pk=None):
        data_fetched = EmployeeModel.objects.get(pk=pk)
        data_fetched.delete()
        return Response(data={'detail':'Deleted Successfully !!!'})

"""-------------------------------------------- or --------------------------------------------------------------------"""


class EmployeeModelViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = EmployeeModel.objects.all()






