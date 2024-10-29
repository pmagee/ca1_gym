from django.urls import path
from .views import GymListView, GymDetailView, GymCreateView, GymUpdateView, GymEquipListView
from . import views

urlpatterns = [
    path('gymlist/', GymListView.as_view(), name='gym_list'),
    path('<int:pk>/', GymDetailView.as_view(), name='gym_detail'),
    path('new/', GymCreateView.as_view(), name='gym_create'),
    path('<int:pk>/edit/', GymUpdateView.as_view(), name='gym_edit'),
    path('gelist/', GymEquipListView.as_view(), name='gymequip_list'),
    path('query1/', views.query1, name='query1'),
    path('query2/', views.query2, name='query2'),
    path('queries/', views.QueryLinksView.as_view(), name='queries'),
]

