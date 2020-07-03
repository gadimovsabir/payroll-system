from django.db import models
from datetime import date

# Create your models here.

GENDER_CHOICES = (
    ('K', 'Kişi'),
    ('Q', 'Qadın')
)

FAMILY_STATUS_CHOICES = (
    ('E', 'Evli'),
    ('S', 'Subay')
)

EDUCATION_CHOICES = (
    ('A', 'Ali'),
    ('O', 'Orta'),
    ('Y', 'Yoxdur'),
)


class Employee(models.Model):
    first_name = models.CharField('Adı', max_length=30)
    last_name = models.CharField('Soyadı', max_length=30)
    father_name = models.CharField('Atasının adı', max_length=30, blank=True)
    date_of_birth = models.DateField('Doğum tarixi')
    gender = models.CharField('Cinsi', max_length=1, choices=GENDER_CHOICES)
    family_status = models.CharField('Ailə vəziyyəti', max_length=1, choices=FAMILY_STATUS_CHOICES)
    education = models.CharField('Təhsili', max_length=1, blank=True, choices=EDUCATION_CHOICES)
    passport_number = models.CharField('Vəsiqənin seriya nömrəsi', max_length=8, unique=True, blank=True, null=True)
    registered_place = models.CharField('Qeydiyyatda olduğu yer', max_length=45, blank=True)
    city_of_residence = models.CharField('Yaşadığı şəhər/kənd', max_length=45, blank=True)
    address = models.CharField('Ünvanı', max_length=50, blank=True)
    contact_number = models.CharField('Əlaqə nömrəsi', max_length=30)
    contact_number2 = models.CharField('Əlaqə nömrəsi əlavə', max_length=30, blank=True)
    photo = models.ImageField('Şəkli', blank=True)

    class Meta:
        verbose_name = 'İşçi'
        verbose_name_plural = 'İşçilər'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_age(self):
        today = date.today()
        difference = today.year - self.date_of_birth.year
        return difference - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))


class OldWorkPlace(models.Model):
    company_name = models.CharField('İşlədiyi şirkətin adı', max_length=255)
    position = models.CharField('İşlədiyi vəzifə', max_length=45)
    started_work = models.DateField('İşə başladığı tarix')
    finished_work = models.DateField('İşdən çıxma tarixi')
    reason_of_leave = models.CharField('İşdən çıxma səbəbi', max_length=255, blank=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name='İşçi')

    class Meta:
        verbose_name = 'Köhnə iş yeri'
        verbose_name_plural = 'Köhnə iş yerləri'
        db_table = 'hr_old_work_place'


class Company(models.Model):
    name = models.CharField('Şirkətin adı', max_length=255, unique=True)

    class Meta:
        verbose_name = 'Şirkət'
        verbose_name_plural = 'Şirkətlər'

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField('Şöbə', max_length=50, unique=True)
    company = models.ManyToManyField(Company, verbose_name='Şirkətlər')

    class Meta:
        verbose_name = 'Şöbə'
        verbose_name_plural = 'Şöbələr'

    def __str__(self):
        return self.name


class Branch(models.Model):
    name = models.CharField('Filialın adı', max_length=50)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, verbose_name='Şirkətin adı', null=True)

    class Meta:
        verbose_name = 'Filial'
        verbose_name_plural = 'Filiallar'

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField('İxtisas', max_length=50, unique=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, verbose_name='Şöbə', blank=True, null=True)

    class Meta:
        verbose_name = 'İxtisas'
        verbose_name_plural = 'İxtisaslar'

    def __str__(self):
        return self.name


class CurrentJob(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, verbose_name='İşçi')
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, verbose_name='Şirkət', null=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, verbose_name='Şöbə', blank=True, null=True)
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, verbose_name='İxtisas', null=True)
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, verbose_name='Filial', blank=True, null=True)
    started_work = models.DateField('İşə başladığı tarix')
    salary = models.IntegerField('Aylıq əmək haqqı')

    class Meta:
        verbose_name = 'Hazırki iş yeri'
        verbose_name_plural = 'Hazırki iş yerləri'
        db_table = 'hr_current_job'
