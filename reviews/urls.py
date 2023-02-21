from . import views
from django.urls import include, path

app_name = "reviews"

urlpatterns = [
    path('', views.index, name='index'),
    path('book-search/', views.search, name='book-search'),
]
