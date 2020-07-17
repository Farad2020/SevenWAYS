from MainApp import views
from django.urls import path, include

app_name = "MainApp"
urlpatterns = [
    path('', views.index, name="index"),
    path('<int:place_id>/', views.place_details, name="place_det"),
]
