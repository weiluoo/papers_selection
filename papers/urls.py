from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('papers/', views.PaperListView.as_view(), name='papers'),
    path('papers/<int:pk>/', views.select_paper, name='select_paper'),
]