from django.urls import path
from service.test import views


urlpatterns = [
    path('', views.index, name='test_index'),
    path('<str:test_id>/', views.detail, name='test_detail')
]
