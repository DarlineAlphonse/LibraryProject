from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Books,User,BookIssue
from .serializers import BooksSerializer
from .serializers import BooksModelSerializer,UserSerializer,IssueBookSerializer
from rest_framework import viewsets
from rest_framework.permissions import BasePermission
from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView,RetrieveAPIView,DestroyAPIView

# Create your views here.
class AdminOnlyPermissions(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if request.method == 'GET':
            return True
        if request.method == 'POST' or request.method == 'PUT' or request.method == 'DELETE':
            if user.is_superuser:
                return True
        return False

#
# class BooksView(APIView):
#     def get(self,request,*args,**kwargs):
#         all_books=Books.objects.all()
#         serializer=BooksSerializer(all_books,many=True)
#         return Response(data=serializer.data)
#
#     def post(self,request,*args,**kwargs):
#         serializer=BooksSerializer(data=request.data)
#         if serializer.is_valid():
#             book_name=serializer.validated_data.get('book_name')
#             category=serializer.validated_data.get('category')
#             author=serializer.validated_data.get('author')
#             available_copies=serializer.validated_data.get('available_copies')
#             book=Books.objects.create(book_name=book_name,category=category,author=author,available_copies=available_copies)
#             return Response(data=serializer.data)
#         else:
#             return Response(data=serializer.errors)
#
# class BookDetailView(APIView):
#     def get(self,request,*args,**kwargs):
#         book_name = kwargs.get('book_name')
#         book=Books.objects.get(book_name=book_name)
#         serializer=BooksSerializer(book)
#         return Response(data=serializer.data)
#
#     def put(self,request,*args,**kwargs):
#         book_name=kwargs.get('book_name')
#         instance=Books.object.get(book_name=book_name)
#         serializer=BooksSerializer(data=request.data)
#         if serializer.is_valid():
#             category = serializer.validated_data.get('category')
#             author = serializer.validated_data.get('author')
#             available_copies = serializer.validated_data.get('available_copies')
#             instance.book_name=book_name
#             instance.category=category
#             instance.author=author
#             instance.available_copies=available_copies
#             return  Response(data=serializer.data)
#         else:
#             return Response(serializer.errors)
#
#     def delete(self,request,*args,**kwargs):
#         book_name=kwargs.get('book_name')
#         book=Books.object.get(book_name=book_name)
#         book.delete()
#         return Response({'msg':'deleted'})

# class BooksViewSet(viewsets.ViewSet):
#     def list(self,request,*args,**kwargs):
#         qs=Books.objects.all()
#         if 'category' in request.query_params:
#             category=request.query_params.get('category')
#             qs=Books.objects.filter(category=category)
#             serializer=BooksModelSerializer(qs,many=True)
#             return Response(serializer.data)
#         if 'author' in request.query_params:
#             author=request.query_params.get('author')
#             qs=Books.objects.filter(author=author)
#             serializer=BooksModelSerializer(qs,many=True)
#             return Response(serializer.data)
#         qs = Books.objects.all()
#         serializer = BooksModelSerializer(qs, many=True)
#         return Response(data=serializer.data)
#
#     def retrieve(self,request,*args,**kwargs):
#         # book_name=kwargs.get('book_name')
#         # qs=Books.objects.get(book_name=book_name)
#         id = kwargs.get('id')
#         qs = Books.objects.get(book_name=id)
#         serializer=BooksModelSerializer(qs)
#         return Response(data=serializer.data)
#
#
# class BooksViewSetRestrictedView(viewsets.ViewSet):
#     permission_classes = AdminOnlyPermissions
#     def create(self,request,*args,**kwargs):
#         serializer=BooksModelSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data)
#         else:
#             return Response(data=serializer.errors)
#
#     def update(self,request,*args,**kwargs):
#         book_name=kwargs.get('book_name')
#         instance=Books.objects.get(book_name=book_name)
#         serializer=BooksModelSerializer(instance=instance,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data)
#         else:
#             return Response(data=serializer.errors)
#
#     def destroy(self,request,*args,**kwargs):
#         book_name=kwargs.get('book_name')
#         qs=Books.objects.get(book_name=book_name)
#         qs.delete()
#         return Response({'message':"deleted"})
#
# class BookModelViewSetView(viewsets.ModelViewSet):
#     permission_classes = AdminOnlyPermissions
#     serializer_class = BooksModelSerializer
#     queryset = Books.objects.all()
#     model=Books

class ListBooksView(ListAPIView):
    serializer_class = BooksModelSerializer
    queryset = Books.objects.all()

class BookCreateView(CreateAPIView):
    permission_classes = AdminOnlyPermissions
    serializer_class = BooksModelSerializer

class UpdateBookView(UpdateAPIView):
    permission_classes = AdminOnlyPermissions
    serializer_class = BooksModelSerializer
    queryset = Books.objects.all()

class BookDetailView(RetrieveAPIView):
    serializer_class = BooksModelSerializer
    queryset = Books.objects.all()

class BookDeleteView(DestroyAPIView):
    permission_classes = AdminOnlyPermissions
    queryset = Books.objects.all()

class NewStudentView(CreateAPIView):
    permission_classes = AdminOnlyPermissions
    serializer_class = UserSerializer

class ListAllStudents(ListAPIView):
    permission_classes = AdminOnlyPermissions
    serializer_class = UserSerializer
    queryset = User.objects.filter(is_superuser=False)

class UserDetailView(RetrieveAPIView):
    permission_classes = AdminOnlyPermissions
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UpdateUserView(UpdateAPIView):
    permission_classes = AdminOnlyPermissions
    serializer_class = UserSerializer
    queryset = User.objects.all()

class RemoveUserView(DestroyAPIView):
    permission_classes = AdminOnlyPermissions
    queryset = User.objects.all()

class IssuedBooksView(ListAPIView):
    permission_classes = (AdminOnlyPermissions,)
    serializer_class = IssueBookSerializer
    queryset = BookIssue.objects.all()

class CreateBookIssue(CreateAPIView):
    permission_classes = (AdminOnlyPermissions,)

    def create(self, request, *args, **kwargs):
        serializer = IssueBookSerializer(data=request.data)
        try:
            book = Books.objects.get(id=request.data.get('book'))
            required_quantity = request.data.get('quantity')

            if not book.is_available:
                return Response('This book is Out of stock')
            if required_quantity > book.quantity:
                return Response('Quantity should be less than or equal to the available quantity')

            elif serializer.is_valid():
                book.quantity -= required_quantity
                book.save()
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        except:
            return Response('No such book available')

class IssuedBookUpdateView(UpdateAPIView):
    permission_classes = (AdminOnlyPermissions,)

    def update(self, request, *args, **kwargs):

        try:
            book = Books.objects.get(id=request.data.get('book'))
            instance = BookIssue.objects.get(id=kwargs.get('pk'))
            serializer = IssueBookSerializer(data=request.data, instance=instance)
            required_quantity = request.data.get('quantity')
            available_qty=Books.objects.get(available_copies='available_copies')
            if available_qty==0:
                return Response('this book is out of stock')
            elif serializer.is_valid():
                    if required_quantity > instance.quantity:
                        book.quantity -= required_quantity - instance.quantity
                        book.save()
                    elif required_quantity < instance.quantity:
                        book.quantity += instance.quantity - required_quantity
                        book.save()
                        serializer.save()
                        return Response(serializer.data)
                    else:
                        return Response(serializer.errors)
                # if not book.is_available and required_quantity > instance.quantity:
                #     return Response('This book is Out of stock')
                # if required_quantity > book.quantity + instance.quantity:
                #     return Response('sorry limit reached')
                #
                # elif serializer.is_valid():
                #     if required_quantity > instance.quantity:
                #         book.quantity -= required_quantity - instance.quantity
                #         book.save()
                #     elif required_quantity < instance.quantity:
                #         book.quantity += instance.quantity - required_quantity
                #         book.save()
                #         serializer.save()
                #         return Response(serializer.data)
                # else:
                #     return Response(serializer.errors)
        except:
            return Response('book unavailable')






