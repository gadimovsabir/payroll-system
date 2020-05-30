from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class Index(TemplateView):
    template_name = 'hr/index.html'


class AddEmployee(TemplateView):
    template_name = 'hr/add_employee.html'
