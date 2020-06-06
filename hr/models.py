from django.db import models

# Create your models here.


class Employee(models.Model):
    first_name = models.CharField('adı', max_length=30)
    last_name = models.CharField('soyadı', max_length=30)
    father_name = models.CharField('atasının adı', max_length=30, blank=True)
    date_of_birth = models.DateField('doğum tarixi')
    gender = models.CharField(
        'cinsi',
        max_length=1,
        choices=[
            ('K', 'kişi'),
            ('Q', 'qadın')
        ]
    )
    family_status = models.CharField(
        'ailə vəziyyəti',
        max_length=1,
        choices=[
            ('E', 'evli'),
            ('S', 'subay')
        ]
    )
    education = models.CharField(
        'təhsili',
        max_length=1,
        blank=True,
        choices=[
            ('A', 'ali'),
            ('O', 'orta'),
            ('Y', 'yoxdur')
        ]
    )
    passport_number = models.CharField(
        'vəsiqənin seriya nömrəsi',
        max_length=8,
        unique=True,
        blank=True,
        null=True
    )
    registered_place = models.CharField('qeydiyyat yeri', max_length=45, blank=True)

    class Meta:
        verbose_name = 'İşçi'
        verbose_name_plural = 'İşçilər'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
