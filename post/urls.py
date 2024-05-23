from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('delete/<int:post_id>/',views.delete),
    path('likes/<int:post_id>/',views.like_count),
    path('edit/<int:post_id>/',views.edit)
    
    ]