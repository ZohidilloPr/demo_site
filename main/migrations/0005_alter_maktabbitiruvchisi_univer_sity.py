# Generated by Django 4.0.6 on 2022-08-15 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_bitiruvchi_jins'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maktabbitiruvchisi',
            name='univer_sity',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name="Topshirmoqchi bo'lgan universitet"),
        ),
    ]
