from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse

from . import forms
from . import models

# Create your views here.


class Index(TemplateView):
    template_name = 'hr/index.html'

    def get(self, request, *args, **kwargs):
        employees = models.Employee.objects.raw("""SELECT * FROM hr_employee
    LEFT JOIN hr_current_job ON hr_employee.id = hr_current_job.employee_id
    LEFT JOIN hr_position ON hr_current_job.position_id = hr_position.id
    LEFT JOIN hr_company ON hr_current_job.company_id = hr_company.id;""")

        return self.render_to_response({'employees': employees})


class AddEmployee(TemplateView):
    template_name = 'hr/add_employee.html'
    employee_form = forms.EmployeeForm()
    old_work_place_form = forms.OldWorkPlaceForm()
    current_job_form = forms.CurrentJobForm()
    actions = (
        '_add_employee',
        '_add_another',
        '_add_and_pass',
        '_pass',
        '_set_work_place'
    )

    def get(self, request, *args, **kwargs):
        try:
            employee = models.Employee.objects.get(id=int(request.GET['id']))
        except (KeyError, ValueError, models.Employee.DoesNotExist):
            return self.render_to_response({'employee_form': self.employee_form})
        
        if request.GET.get('form') == 'old_work_place_form':
            return self.render_to_response({
                'old_work_place_form': self.old_work_place_form,
                'employee_id': employee.id
            })

        if request.GET.get('form') == 'current_job_form':
            return self.render_to_response({
                'current_job_form': self.current_job_form,
                'employee_id': employee.id
            })
        
        return self.render_to_response({'employee_form': self.employee_form})

    def post(self, request, *args, **kwargs):
        for action in self.actions:
            if request.POST.get(action):
                try:
                    return eval(f'self.{action}(request)')
                except self.InvalidData:
                    return HttpResponseRedirect(reverse('hr:add_employee'))

        return HttpResponseRedirect(reverse('hr:add_employee'))

    def _add_employee(self, request):
        employee_form = forms.EmployeeForm(request.POST, request.FILES)

        if employee_form.is_valid():
            employee_id = employee_form.save().id
            return HttpResponseRedirect(
                '/hr/addemployee/' + f'?id={employee_id}&form=old_work_place_form'
            )

        return self.render_to_response({'employee_form': employee_form})

    def _add_another(self, request):
        employee = self._get_employee(request)
        old_work_place_form = forms.OldWorkPlaceForm(request.POST)

        if old_work_place_form.is_valid():
            self._create_old_work_place(old_work_place_form.cleaned_data, employee)
            return HttpResponseRedirect(
                '/hr/addemployee/' + f'?id={employee.id}&form=old_work_place_form'
            )

        return self.render_to_response({
            'old_work_place_form': old_work_place_form,
            'employee_id': employee.id
        })

    def _add_and_pass(self, request):
        employee = self._get_employee(request)
        old_work_place_form = forms.OldWorkPlaceForm(request.POST)

        if old_work_place_form.is_valid():
            self._create_old_work_place(old_work_place_form.cleaned_data, employee)
            return HttpResponseRedirect(
                '/hr/addemployee/' + f'?id={employee.id}&form=current_job_form'
            )

        return self.render_to_response({
            'old_work_place_form': old_work_place_form,
            'employee_id': employee.id
        })

    def _pass(self, request):
        return HttpResponseRedirect(
            '/hr/addemployee/' + f'?id={self._get_employee(request).id}&form=current_job_form'
        )

    def _set_work_place(self, request):
        employee = self._get_employee(request)
        current_job_form = forms.CurrentJobForm(request.POST)

        if current_job_form.is_valid():
            models.CurrentJob.objects.create(
                company=current_job_form.cleaned_data['company'],
                department=current_job_form.cleaned_data['department'],
                position=current_job_form.cleaned_data['position'],
                branch=current_job_form.cleaned_data['branch'],
                started_work=current_job_form.cleaned_data['started_work'],
                salary=current_job_form.cleaned_data['salary'],
                employee=employee
            )
            return HttpResponseRedirect(f'/hr/{employee.id}/')

        return self.render_to_response({
            'current_job_form': current_job_form,
            'employee_id': employee.id
        })

    def _create_old_work_place(self, cleaned_data, employee):
        models.OldWorkPlace.objects.create(
            company_name=cleaned_data['company_name'],
            position=cleaned_data['position'],
            started_work=cleaned_data['started_work'],
            finished_work=cleaned_data['finished_work'],
            reason_of_leave=cleaned_data['reason_of_leave'],
            employee=employee
        )

    def _get_employee(self, request):
        try:
            return models.Employee.objects.get(id=request.POST['employee'])
        except (KeyError, models.Employee.DoesNotExist):
            raise self.InvalidData

    class InvalidData(Exception):
        pass


class EmployeeDetail(TemplateView):
    template_name = 'hr/employee_detail.html'

    def get(self, request, pk, *args, **kwargs):
        employee = get_object_or_404(models.Employee, pk=pk)
        context = {'employee': employee}

        if request.GET.get('form') == 'vacation_form':
            context['form'] = forms.VacationForm()

        return self.render_to_response(context)

    def post(self, request, *args, **post):
        vacation_form = forms.VacationForm(request.POST)

        try:
            employee = models.Employee.objects.get(pk=request.POST['employee'])
            current_job = models.CurrentJob.objects.get(employee_id=employee.id)
        except (KeyError, models.Employee.DoesNotExist):
            return HttpResponseRedirect(reverse('hr:index'))
        except models.CurrentJob.DoesNotExist:
            vacation_form.add_error(None, 'İşçi iş yerinə təyin edilməyib.')

        if vacation_form.is_valid():
            vacation_form.save()
            current_job.count_since = vacation_form.cleaned_data['end_of_vacation']
            current_job.save()
            return self.render_to_response({'employee': employee})

        return self.render_to_response({
            'employee': employee,
            'form': vacation_form
        })


class DeleteEmployee(TemplateView):
    template_name = 'hr/delete_confirmation.html'

    def get(self, request, pk, *args, **kwargs):
        employee = get_object_or_404(models.Employee, pk=pk)
        return self.render_to_response({'employee': employee})

    def post(self, request, pk, *args, **kwargs):
        try:
            employee = models.Employee.objects.get(pk=pk)
            employee.delete()
        finally:
            return HttpResponseRedirect(reverse('hr:index'))


class ChangeEmployee(TemplateView):
    template_name = 'hr/change_employee.html'

    def get(self, request, pk, *args, **kwargs):
        employee = get_object_or_404(models.Employee, pk=pk)
        return self.render_to_response({
            'employee_form': forms.EmployeeForm(instance=employee)
            })
    
    def post(self, request, pk, *args, **kwargs):
        employee = get_object_or_404(models.Employee, pk=pk)
        employee_form = forms.EmployeeForm(request.POST, request.FILES, instance=employee)

        if employee_form.is_valid():
            employee_form.save()
            return HttpResponseRedirect(f'/hr/{pk}/')

        return self.render_to_response({'employee_form': employee_form})


class Vacations(TemplateView):
    template_name = 'hr/vacations.html'

    def get(self, request, *args, **kwargs):
        vacations = models.Vacation.objects.all()
        return self.render_to_response({'vacations': vacations})
