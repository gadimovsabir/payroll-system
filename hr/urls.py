from django.urls import path

from . import views

app_name = 'hr'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('addemployee/', views.AddEmployee.as_view(), name='add_employee'),
    path('<int:pk>/', views.EmployeeDetail.as_view(), name='employee_detail'),
    path('<int:pk>/delete/', views.DeleteEmployee.as_view(), name='delete_employee'),
]
