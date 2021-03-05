from django.urls import path

from . import views

app_name = "firstsite"

urlpatterns = [
    #/
    path('', views.index, name='index'),
    #/music/
    path('music/', views.music, name='music'),
    #/music/[0-9]+
    path('music/<int:album_id>/', views.albums, name='album'),
    #/add/
    path('add', views.add, name='add')
]
