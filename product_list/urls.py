from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='lists'),
    path('list/<int:pk>/', views.get_product_list, name='list_details'),
    path('new_list/', views.new_product_list, name ='new_product_list'),
]