from django.urls import path
from . import views

urlpatterns = [
    path('country_create/', views.Country_Create.as_view()),
    path('', views.data_page)
]