# Generated by Django 4.0.6 on 2022-08-09 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_kollejbitiruvchisi_univer_sity_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bitiruvchi',
            name='jins',
            field=models.CharField(choices=[("o'g'il bola", "o'g'il bola"), ('qiz bola', 'qiz bola')], default="o'g'il bola", max_length=300, verbose_name='Jinsi'),
        ),
    ]