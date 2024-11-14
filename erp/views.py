from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from .models import Category, Student, Article, Comment, Author
from .serializers import StudentSerializer


# Create your views here.

class IndexApiView(APIView):
    def get(self, request: Request):
        return Response({"message": "salom Dunyo"})


class Converter(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', ]
class CategoryView(APIView):

    def get(self, request: Request, pk=None):
        if pk:
            categ = Converter(Category.objects.get(pk=pk))
            return Response(categ.data)
        objects = Converter(Category.objects.all(), many=True)
        return Response(objects.data)

    def post(self, request: Request):
        post_data = Category.objects.create(name=request.data.get('name'))
        post_data.save()
        return Response(request.data)

    def put(self, request: Request, pk:int):
        try:
            categ = Category.objects.get(pk=pk)
            categ.name = request.data.get('name', categ.name)
            categ.save()
            return Response("Successfully updated")
        except Category.DoesNotExist:
            return Response("Category not found", status=status.HTTP_404_NOT_FOUND)

    def delete(self, request: Request, pk=int):
        try:
            categ = Category.objects.get(pk=pk)
            categ.delete()
            return Response({"message": "Category deleted successfully"})
        except:
            return Response(status=404)

class Student_conv(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['group', 'full_name', 'age', 'address', 'phone_number', 'email']
class StudentView(APIView):
    def get(self, requet: Request):
        objects = Student_conv(Student.objects.all(), many=True)
        return  Response(objects.data)



class Article_conv(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['title', 'content', 'date_posted', 'category', 'author']
class ArticleView(APIView):

    def get(self, request: Request, pk=None):
        if pk:
            objects = Article_conv(Article.objects.get(pk=pk))
            return Response(objects.data)
        objects = Article_conv(Article.objects.all(), many=True)
        return Response(objects.data)

    def post(self, request: Request):
        category_id = request.data.get('category')
        category = Category.objects.get(pk=category_id) if category_id else None

        post_data = Article.objects.create(
            title=request.data.get('title'),
            content=request.data.get('content'),
            date_posted=request.data.get('date_posted'),
            category=category,
            author=request.data.get('author'),
            )
        post_data.save()
        print(request.data.get('title'))
        return Response(request.data)

    def put(self, request: Request, pk: int):

        category_id = request.data.get('category')
        category = Category.objects.get(pk=category_id) if category_id else None
        try:
            categ = Article.objects.get(pk=pk)
            categ.title = request.data.get('title')
            categ.content = request.data.get('content')
            categ.date_posted = request.data.get('date_posted')
            categ.category = category
            categ.author = request.data.get('author')
            categ.save()
            return Response("Successfully updated")
        except Category.DoesNotExist:
            return Response("Category not found", status=status.HTTP_404_NOT_FOUND)

    def delete(self, request: Request, pk=int):
        try:
            categ = Article.objects.get(pk=pk)
            categ.delete()
            return Response({"message": "Category deleted successfully"})
        except:
            return Response(status=404)


class Comment_conv(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['article', 'username', 'email', 'content', 'date_posted']
class CommentView(APIView):

    def get(self, request: Request):
        objects = Comment_conv(Comment.objects.all(), many=True)
        return Response(objects.data)



class Authorconv(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['full_name', 'username', 'email']
class AuthorView(APIView):

    def get(self, request: Request):
        objects = Authorconv(Author.objects.all(), many=True)
        return Response(objects.data)