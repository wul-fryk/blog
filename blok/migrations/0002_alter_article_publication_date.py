# Generated by Django 4.0.6 on 2022-07-17 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blok', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='publication_date',
            field=models.DateTimeField(),
        ),
    ]
