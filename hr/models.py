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
        default='K',
        choices=[
            ('K', 'kişi'),
            ('Q', 'qadın')
        ]
    )
    family_status = models.CharField(
        'ailə vəziyyəti',
        max_length=1,
        default='E',
        choices=[
            ('E', 'evli'),
            ('S', 'subay')
        ]
    )
    education = models.CharField(
        'təhsili',
        max_length=1,
        blank=True,
        default='A',
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
    contact_number = models.CharField('əlaqə nömrəsi', max_length=30, blank=True)
    contact_number2 = models.CharField('əlaqə nömrəsi əlavə', max_length=30, blank=True)
    registered_place = models.CharField('qeydiyyatda olduğu yer', max_length=45, blank=True)
    city_of_residence = models.CharField('yaşadığı şəhər/kənd', max_length=45, blank=True)
    address = models.CharField('ünvanı', max_length=50, blank=True)
    photo = models.ImageField('şəkli', unique=True, blank=True, null=True)

    class Meta:
        verbose_name = 'İşçi'
        verbose_name_plural = 'İşçilər'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class OldWorkPlace(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name='işçi')
    company_name = models.CharField('işlədiyi şirkətin adı', max_length=250)
    position = models.CharField('vəzifəsi', max_length=45)
    started = models.DateField('işə başladiğı tarix')
    finished = models.DateField('işdən çıxma tarixi')
    cause = models.TextField('işdən çıxma səbəbi', blank=False)

    class Meta:
        verbose_name = 'köhnə iş yeri'
        verbose_name_plural = 'köhnə iş yerləri'
