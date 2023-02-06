from  .serializers import BlogSerializer, BlogModel
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, ListAPIView  #(post, get)
from rest_framework.generics import RetrieveAPIView, UpdateAPIView, DestroyAPIView, RetrieveUpdateDestroyAPIView


class BlogGenericAPI(CreateAPIView, ListAPIView):
    serializer_class = BlogSerializer
    queryset = BlogModel.objects.all()
    


class BlogPostDetailView(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
    serializer_class = BlogSerializer
    queryset = BlogModel.objects.all()
    

class BlogDetailCombineView(RetrieveUpdateDestroyAPIView):
    serializer_class = BlogSerializer
    queryset = BlogModel.objects.all()

