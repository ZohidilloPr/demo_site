# Generated by Django 4.0.6 on 2022-08-17 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_kollejbitiruvchisi_stu_way_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bitiruvchi',
            name='t_sana',
            field=models.DateField(blank=True, null=True, verbose_name="Tug'ulgan sana"),
        ),
    ]