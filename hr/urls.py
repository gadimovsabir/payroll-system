from django.urls import path

from . import views

app_name = 'hr'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('add', views.AddEmployee.as_view(), name='add_employee'),
]
