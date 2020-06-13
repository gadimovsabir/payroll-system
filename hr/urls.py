from django.urls import path
from django.conf.urls.static import static

from . import views
from PayrollSystem import settings

app_name = 'hr'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('addemployee/', views.AddEmployee.as_view(), name='add_employee'),
    path('<int:pk>/', views.EmployeeDetail.as_view(), name='employee_detail'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
