from django import forms
from django.core.validators import RegexValidator

from . import models

EMPLOYEE_NAME_VALIDATOR = RegexValidator(
    regex=r'^[A-ZÜİÖĞƏÇŞ]{1}[a-züöğıəçş]{1,29}$',
    message='Düzgün məlumat daxil edin.',
)

NUMBER_VALIDATOR = RegexValidator(
    regex=r'^\+?[0-9]{5,29}$',
    message='Düzgün məlumat daxil edin.'
)

PLACE_NAME_VALIDATOR = RegexValidator(
    regex=r'^[A-VX-ZÜİÖĞƏÇŞa-vx-züöğıəçş]{3,45}$',
    message='Düzgün məlumat daxil edin.'
)


class EmployeeForm(forms.ModelForm):
    first_name = forms.CharField(label='Adı', validators=[EMPLOYEE_NAME_VALIDATOR]  )
    last_name = forms.CharField(label='Soyadı', validators=[EMPLOYEE_NAME_VALIDATOR])
    father_name = forms.CharField(
        label='Atasının adı',
        validators=[EMPLOYEE_NAME_VALIDATOR],
        required=False
    )
    passport_number = forms.RegexField(
        regex=r'^[0-9]{8}$',
        max_length=8,
        min_length=8,
        label='Vəsiqənin seriya nömrəsi',
        error_messages={
            'invalid': 'Məlumat yanlışdı, 8 rəqəm olmalıdı.',
            'unique': 'Bu seriya nömrəsi ilə işçi artıq mövcuddur.'
        },
        required=False,
    )
    registered_place = forms.CharField(
        label='Qeydiyyatda olduğu yer',
        validators=[PLACE_NAME_VALIDATOR],
        required=False
    )
    city_of_residence = forms.CharField(
        label='Yaşadığı şəhər/kənd',
        validators=[PLACE_NAME_VALIDATOR],
        required=False
    )
    address = forms.RegexField(
        regex=r'^[A-VX-ZÜİÖĞƏÇŞa-vx-züöğıəçş0-9. ]{3,50}$',
        label='Ünvanı',
        required=False,
        error_messages={'invalid': 'Düzgün məlumat daxil edin.'}
    )
    contact_number = forms.CharField(label='Əlaqə nömrəsi', validators=[NUMBER_VALIDATOR])
    contact_number2 = forms.CharField(
        label='Əlaqə nömrəsi əlavə',
        validators=[NUMBER_VALIDATOR],
        required=False
    )

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

    def clean_passport_number(self):
        passport_number = self.cleaned_data['passport_number']
        if passport_number == '':
            return None

        return passport_number


class OldWorkPlaceForm(forms.ModelForm):
    company_name = forms.RegexField(
        regex=r'^[A-ZÜİÖĞƏÇŞa-züöğıəçş0-9\-\'.&+ ]{3,255}$',
        label='İşlədiyi şirkətin adı',
        error_messages={
            'invalid': 'Şirkətin adında hərflər, rəqəmlər və yalnız bu [\'&+-. ] simvollar ola bilər.'
        }
    )
    position = forms.RegexField(
        regex=r'^[a-züöğıəçş]{3,45}( [a-züöğıəçş]{3,41}){0,2}$',
        label='İşlədiyi vəzifə',
        error_messages={'invalid': 'Düzgün məlumat daxil edin, yalnız kiçik hərflər.'}
    )

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
            'employee': forms.HiddenInput
        }


class CurrentJobForm(forms.ModelForm):
    salary = forms.IntegerField(
        label='Aylıq əmək haqqı',
        min_value=100,
        max_value=1e5,
        error_messages={
            'min_value': 'Əmək haqqı 100-dən az olammaz.',
            'max_value': 'Əmək haqqı 100.000-dən çox olammaz.'
        }
    )

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
            'employee': forms.HiddenInput
        }
