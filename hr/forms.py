from django.forms import ModelForm

from . import models


class EmployeeForm(ModelForm):
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
            'contact_number',
            'contact_number2',
            'city_of_residence',
            'address',
            'photo',
        ]

        error_messages = {
            'passport_number': {
                'unique': 'Bu seriya nömrəsi ilə işçi artıq mövcuddur',
            },
        }
