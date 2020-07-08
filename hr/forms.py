from django import forms

from . import models


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = models.Employee
        fields = [
            'first_name',
            'last_name',
            'father_name',
            'date_of_birth',
            'gender',
            'family_status',
            'education',
            'passport_number',
            'registered_place',
            'city_of_residence',
            'address',
            'contact_number',
            'contact_number2',
            'photo'
        ]

        widgets = {
            'date_of_birth': forms.DateInput(attrs={'class': 'date-field'})
        }


class OldWorkPlaceForm(forms.ModelForm):
    class Meta:
        model = models.OldWorkPlace
        fields = [
            'company_name',
            'position',
            'started_work',
            'finished_work',
            'reason_of_leave',
            'employee'
        ]

        widgets = {
            'employee': forms.HiddenInput,
            'started_work': forms.DateInput(attrs={'class': 'date-field'}),
            'finished_work': forms.DateInput(attrs={'class': 'date-field'})
        }


class CurrentJobForm(forms.ModelForm):
    class Meta:
        model = models.CurrentJob
        fields = [
            'company',
            'department',
            'position',
            'branch',
            'started_work',
            'salary',
            'employee'
        ]

        widgets = {
            'employee': forms.HiddenInput,
            'started_work': forms.DateInput(attrs={'class': 'date-field'})
        }
