# Generated by Django 4.0 on 2022-01-22 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inheritanceapp', '0012_artifact_category_alter_artifact_imgfilter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artifact',
            name='category',
            field=models.CharField(choices=[('artistic', 'artistic'), ('beautiful', 'beautiful'), ('profound', 'profound')], default='artistic', max_length=25),
        ),
    ]
