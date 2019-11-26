from django.urls import path
from . import views

app_name = 'laptops'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:program_pk>/', views.detail, name = 'detail'),
]
