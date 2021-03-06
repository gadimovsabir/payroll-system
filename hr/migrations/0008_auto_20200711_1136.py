# Generated by Django 3.0.6 on 2020-07-11 07:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0007_currentjob'),
    ]

    operations = [
        migrations.AddField(
            model_name='currentjob',
            name='count_since',
            field=models.DateField(null=True),
        ),
        migrations.CreateModel(
            name='Vacation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_of_vacation', models.DateField(verbose_name='Məzuniyyətin ilk günü')),
                ('end_of_vacation', models.DateField(verbose_name='Məzuniyyətin bitdiyi gün')),
                ('type_of_vacation', models.CharField(choices=[('1type', 'Əmək məzuniyyəti'), ('2type', 'Sosisal məzuniyyət'), ('3type', 'Ödənişsiz məzuniyyət')], max_length=5, verbose_name='Məzuniyyətin növü')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.Employee', verbose_name='İşçi')),
            ],
            options={
                'verbose_name': 'Məzuniyyət',
                'verbose_name_plural': 'Məzuniyyətlər',
            },
        ),
    ]
