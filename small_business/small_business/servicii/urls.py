from django.contrib import admin
from django.urls import path

from home.views import HomeView

from servicii.views import ServiciiDetailView, ServiciiListView, ServiciiUpdateView, ServiciiDeleteView, \
    ServiciiCreateView

urlpatterns = [
    path('', ServiciiListView.as_view(), name='serviciu-all'),
    path('detail/<int:pk>', ServiciiDetailView.as_view(), name='serviciu-detail'),
    path('update/<int:pk>', ServiciiUpdateView.as_view(), name='serviciu-edit'),
    path('delete/<int:pk>', ServiciiDeleteView.as_view(), name='serviciu-delete'),
    path('add/', ServiciiCreateView.as_view(), name='add-serviciu'),
]