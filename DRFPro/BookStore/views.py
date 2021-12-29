from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from rest_framework.views import APIView
from rest_framework import generics
from .serializer import *
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthorOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_jwt.utils import jwt_decode_handler

@api_view(['GET'])
def BookList(request):

    allbook = Book.objects.all()
    ser = BookSerializer(allbook,many=True)
    return Response(data = ser.data)


class BookAPIView(APIView):
    def get(self,request,*args,**kwargs):
        allbook = Book.objects.all()
        ser = BookSerializer(allbook, many=True)
        return Response(data=ser.data)

    def post(self,request):
        ser = BookSerializer(data = request.data)
        if ser.is_valid():
            ser.save()
            return Response(data=ser.data)
        else:
            return Response(data={"error":"Something went wrong"})



class BookMixinView(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request,*args, **kwargs)

    def post(self,request,*args, **kwargs):
        return self.create(request,*args, **kwargs)



class AdvanceBookView(generics.ListAPIView):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'author','book_type','favbook']
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BookDetailView(generics.RetrieveAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

class BookCreateView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BookSerializer

    def post(self,request):
        #print(request.headers)
        token = request.headers.get('Authorization')[4:]
        decode_data = jwt_decode_handler(token=token)
        #print(decode_data)
        userId = decode_data['user_id']
        ser = BookSerializer(data = request.data)
        if ser.is_valid():
            ser.save()
            ser.validated_data['author'] = User.objects.get(id = userId)
            ser.save()
            return Response(data={"book":ser.data})
        else:
            return Response(data={"error": "Something went Wrong"})






class CategoryWiseBook(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        genre_id = int(self.kwargs['pk'])
        genredata = Genre.objects.filter(id = genre_id).first()
        if genredata:
            return Book.objects.filter(category = genredata)
        else:
            return []

class BookDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated,IsAuthorOrReadOnly]
    serializer_class = BookSerializer
    queryset = Book.objects.all()

class BookUpdateView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated,IsAuthorOrReadOnly]
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class RegisterUserView(APIView):

    def post(self, request):
        ser = RegisterUserSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(data=ser.data)
        else:
            return Response(data={"error":ser.errors })


class UserBooks(generics.ListAPIView):
    serializer_class = BookSerializer
    def get_queryset(self):
        token = self.request.query_params.get('usertoken')
        print(token)
        decode_data = jwt_decode_handler(token=token)
        username = decode_data['username']
        return Book.objects.filter(author__username=username)


class CategoryList(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Genre.objects.all()

#JWT  - JSON WEB TOKEN
















































