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
    employee_form = forms.EmployeeForm()
    old_work_place_form = forms.OldWorkPlaceForm()
    actions = (
        '_add_employee',
        '_add_another',
    )

    def get(self, request, *args, **kwargs):
        return self.render_to_response({'employee_form': self.employee_form})

    def post(self, request, *args, **kwargs):
        for action in self.actions:
            if request.POST.get(action):
                return eval(f'self.{action}(request)')

        return self.render_to_response({'employee_form': self.employee_form})

    def _add_employee(self, request):
        employee_form = forms.EmployeeForm(request.POST, request.FILES)
        if employee_form.is_valid():
            employee_id = employee_form.save().id
            return self.render_to_response({
                'old_work_place_form': self.old_work_place_form,
                'employee_id': employee_id
            })

        return self.render_to_response({'employee_form': employee_form})

    def _add_another(self, request):
        try:
            employee = models.Employee.objects.get(id=request.POST['employee'])
        except (KeyError, models.Employee.DoesNotExist):
            return self.render_to_response({'employee_form': self.employee_form})

        old_work_place_form = forms.OldWorkPlaceForm(request.POST)

        if old_work_place_form.is_valid():
            employee_id = models.OldWorkPlace.objects.create(
                company_name=request.POST['company_name'],
                position=request.POST['position'],
                started=request.POST['started'],
                finished=request.POST['finished'],
                cause=request.POST['cause'],
                employee=employee
            ).employee.id

            return self.render_to_response({
                'old_work_place_form': self.old_work_place_form,
                'employee_id': employee_id
            })

        return self.render_to_response({
            'old_work_place_form': old_work_place_form,
            'employee_id': employee.id
        })


class EmployeeDetail(TemplateView):
    template_name = 'hr/employee_detail.html'

    def get(self, request, pk, *args, **kwargs):
        employee = get_object_or_404(models.Employee, pk=pk)
        return self.render_to_response({'employee': employee})
