# Generated by Django 4.0.6 on 2022-08-31 05:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_alter_kollejbitiruvchisi_guvohnoma_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bitiruvchi',
            name='millat',
        ),
        migrations.RemoveField(
            model_name='maktabbitiruvchisi',
            name='maqsad',
        ),
    ]