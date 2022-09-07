from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('comment/<int:comment_id>', views.comment_view, name="comment"),
    path('list', views.comment_list, name="list"),
]
