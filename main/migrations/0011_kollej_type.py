# Generated by Django 4.0.6 on 2022-08-18 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_typekollej_kollejbitiruvchisi_tuman_kj_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='kollej',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.typekollej'),
        ),
    ]
