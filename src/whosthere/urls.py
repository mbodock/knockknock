from django.urls import path

from . import views

urlpatterns = [
    path('update/', views.UpdateHosts.as_view(), name='update'),
]
