from django.shortcuts import render
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from .models import Category, Student, Article, Comment, Author


# Create your views here.

class IndexApiView(APIView):
    def get(self, request: Request):
        return Response({"message": "salom Dunyo"})


class Converter(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', ]
class CategoryView(APIView):

    def get(self, request: Request):
        objects = Converter(Category.objects.all(), many=True)
        return Response(objects.data)


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

    def get(self, request: Request):
        objects = Article_conv(Article.objects.all(), many=True)
        return Response(objects.data)


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