# Generated by Django 4.0.6 on 2022-07-18 12:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('content', models.TextField()),
                ('publication_date', models.DateTimeField()),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Coment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coment', models.TextField()),
                ('coment_publication', models.DateTimeField()),
                ('comented_article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blok.article')),
                ('coments_author', models.ForeignKey(default='profl usunięty', on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
