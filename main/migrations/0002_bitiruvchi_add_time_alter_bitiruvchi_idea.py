# Generated by Django 4.0.6 on 2022-08-16 06:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bitiruvchi',
            name='add_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bitiruvchi',
            name='idea',
            field=models.CharField(choices=[('Bor', 'Bor'), ('Yoq', 'Yoq')], default='Bor', max_length=300, verbose_name="Biznes g'oya"),
        ),
    ]