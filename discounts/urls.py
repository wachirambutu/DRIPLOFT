from django.urls import path
from .import views
urlpatterns = [
 	path('apply/', views.discount_apply),
]