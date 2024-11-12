from django.db import models
from django.contrib.auth.models import Group
from django.core.validators import MaxValueValidator, MinValueValidator
from rest_framework.fields import BooleanField


# Create your models here.


class Student(models.Model):
    group = models.ForeignKey(Group, on_delete=models.PROTECT)
    full_name = models.CharField(max_length=50, verbose_name='toliq-ism')
    age = models.PositiveIntegerField(validators=[
        MinValueValidator(5),
        MaxValueValidator(100)
    ],verbose_name='yosh')
    address = models.CharField(max_length=255, null=True, blank=True, verbose_name='manzil')
    phone_number = models.CharField(max_length=13, verbose_name='telefon')
    email = models.EmailField(verbose_name='email')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Studentlar'


class Category(models.Model):
    name = models.CharField(max_length=75 ,verbose_name='nomi')
    photo = models.ImageField(upload_to='Category-image/', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'kategorya'
        verbose_name_plural = 'kategoryalar'


class Article(models.Model):
    title = models.CharField(max_length=75, verbose_name='sarlavha')
    content = models.TextField(verbose_name='tarkib')
    date_posted = models.DateField(auto_now=True, verbose_name='nashr-sana')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='kategoriya')
    author = models.CharField(max_length=75, verbose_name='muallif')
    photo = models.ImageField(upload_to='Article-image/', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Maqola'
        verbose_name_plural = 'Maqolalar'


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='maqola')
    username = models.CharField(max_length=75, verbose_name='foydalanuvchi-nomi')
    email = models.CharField(max_length=75, verbose_name='email')
    content = models.TextField(verbose_name='matn')
    date_posted = models.DateTimeField(auto_now=True, verbose_name='nashr-sanasi')


    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'sharx'
        verbose_name_plural = 'sharxlar'


class Author(models.Model):
    full_name = models.CharField(max_length=150, verbose_name='toliq-ism')
    username = models.CharField(max_length=75, verbose_name='foydalanuvchi-nomi')
    email = models.CharField(max_length=75, verbose_name='email')
    photo = models.ImageField(upload_to='Author-image/', null=True, blank=True)


    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authorlar'
