# Generated by Django 3.2.7 on 2021-10-20 03:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backendService', '0013_templateselection'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerdata',
            name='template',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backendService.templateselection'),
        ),
    ]
