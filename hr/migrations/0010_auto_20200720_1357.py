# Generated by Django 3.0.6 on 2020-07-20 09:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0009_auto_20200715_0927'),
    ]

    operations = [
        migrations.AddField(
            model_name='currentjob',
            name='pros_and_cons',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Absent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_absence', models.DateField(verbose_name='İşə gəlmədiyi gün')),
                ('reason_of_absence', models.CharField(choices=[('1', 'Üzürlü səbəb'), ('2', 'Üzürsüz səbəb')], max_length=1, verbose_name='İşə gəlməmə səbəbi')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.Employee', verbose_name='İşçi')),
            ],
        ),
    ]
