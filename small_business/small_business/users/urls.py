from django.urls import path

from home.views import HomeView
from users.views import *

urlpatterns = [
    path('', UsersListView.as_view(), name='users-all'),
    path('add/', CreateUserView.as_view(), name='users-add'),
    path('detail/<int:pk>', UserDetailView.as_view(), name='users-detail'),
    path('edit/<int:pk>', UsersUpdateView.as_view(), name='users-edit'),
    path('delete/<int:pk>', UsersDeleteView.as_view(), name='users-delete'),
]