from django.contrib import admin
from .models import Student, Category, Article, Comment, Author


# Register your models here.

admin.site.register(Student)
admin.site.register(Category)
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Author)