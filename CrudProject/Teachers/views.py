from rest_framework.views import APIView
from .serializers import TeacherSerializer, TeachersModel
from rest_framework.response import Response


class TeacherAPIView(APIView):
    serializer_class = TeacherSerializer

    def get(self, request):
        fetched_data = TeachersModel.objects.all()
        de_serializer = self.serializer_class(fetched_data, many=True)
        return Response(data=de_serializer.data)

    def post(self, request):
        data_recieved = request.data
        serializer = self.serializer_class(data=data_recieved)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors)

class TeacherDetailAPIView(APIView):
    serializer_class = TeacherSerializer

    def get(self, request, pk=None):
        fetched_particular = TeachersModel.objects.get(pk=pk)
        des_serializer = self.serializer_class(fetched_particular)
        return Response(data=des_serializer.data)
    
    def put(self, request, pk=None):
        fetched_data = TeachersModel.objects.get(pk=pk)
        serializer = self.serializer_class(data=request.data, instance=fetched_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors)

    def patch(self, request, pk=None):
        fetched_data = TeachersModel.objects.get(pk=pk)
        serializer = self.serializer_class(data=request.data, instance=fetched_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors)
    
    def delete(self, request, pk=None):
        fetched_data = TeachersModel.objects.get(pk=pk)
        fetched_data.delete()
        return Response(data={'detail':'Deleted Successfully !!!'})


