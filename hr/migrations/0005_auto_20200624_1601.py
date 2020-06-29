# Generated by Django 3.0.6 on 2020-06-24 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0004_auto_20200619_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='contact_number',
            field=models.CharField(max_length=30, verbose_name='Əlaqə nömrəsi'),
        ),
        migrations.AlterField(
            model_name='oldworkplace',
            name='position',
            field=models.CharField(max_length=45, verbose_name='İşlədiyi vəzifə'),
        ),
        migrations.AlterField(
            model_name='oldworkplace',
            name='reason_of_leave',
            field=models.CharField(blank=True, max_length=255, verbose_name='İşdən çıxma səbəbi'),
        ),
    ]