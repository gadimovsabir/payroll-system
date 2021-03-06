# Generated by Django 3.0.6 on 2020-06-11 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='address',
            field=models.CharField(blank=True, max_length=50, verbose_name='ünvanı'),
        ),
        migrations.AddField(
            model_name='employee',
            name='city_of_residence',
            field=models.CharField(blank=True, max_length=45, verbose_name='yaşadığı şəhər/kənd'),
        ),
        migrations.AddField(
            model_name='employee',
            name='contact_number',
            field=models.CharField(blank=True, max_length=30, verbose_name='əlaqə nömrəsi'),
        ),
        migrations.AddField(
            model_name='employee',
            name='contact_number2',
            field=models.CharField(blank=True, max_length=30, verbose_name='əlaqə nömrəsi əlavə'),
        ),
        migrations.AddField(
            model_name='employee',
            name='photo',
            field=models.ImageField(blank=True, null=True, unique=True, upload_to='', verbose_name='şəkli'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='education',
            field=models.CharField(blank=True, choices=[('A', 'ali'), ('O', 'orta'), ('Y', 'yoxdur')], default='A', max_length=1, verbose_name='təhsili'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='family_status',
            field=models.CharField(choices=[('E', 'evli'), ('S', 'subay')], default='E', max_length=1, verbose_name='ailə vəziyyəti'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='gender',
            field=models.CharField(choices=[('K', 'kişi'), ('Q', 'qadın')], default='K', max_length=1, verbose_name='cinsi'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='registered_place',
            field=models.CharField(blank=True, max_length=45, verbose_name='qeydiyyatda olduğu yer'),
        ),
    ]
