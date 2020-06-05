from django.shortcuts import render
from django.views.generic import TemplateView

from . import forms
from . import models

# Create your views here.


class Index(TemplateView):
    template_name = 'hr/index.html'

    def get(self, request, *args, **kwargs):
        employees = models.Employee.objects.all()
        return self.render_to_response({'employees': employees})


class AddEmployee(TemplateView):
    template_name = 'hr/add_employee.html'

    def get(self, request, *args, **kwargs):
        form = forms.EmployeeForm()
        return self.render_to_response({'form': form})

    def post(self, request, *args, **kwargs):
        form = forms.EmployeeForm(request.POST)
        if form.is_valid():
            form.save()

        return self.render_to_response({'form': form})
