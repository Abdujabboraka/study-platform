from django.urls import path
from .views import IndexApiView, CategoryView, StudentView, ArticleView, CommentView, AuthorView


urlpatterns=[
    path('', IndexApiView.as_view()),
    path('category/', CategoryView.as_view()),
    path('student/', StudentView.as_view()),
    path('article/', ArticleView.as_view()),
    path('comment/', CommentView.as_view()),
    path('author/', AuthorView.as_view())

]