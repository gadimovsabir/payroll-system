from django.shortcuts import render, get_object_or_404
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
        form = forms.EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

        return self.render_to_response({'form': form})


class EmployeeDetail(TemplateView):
    template_name = 'hr/employee_detail.html'

    def get(self, request, pk, *args, **kwargs):
        employee = get_object_or_404(models.Employee, pk=pk)
        return self.render_to_response({'employee': employee})
