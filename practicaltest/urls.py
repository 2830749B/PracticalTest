from django.urls import path
from practicaltest import views

app_name = 'practicaltest'

urlpatterns = [
    path('', views.index, name='index'),
    ]