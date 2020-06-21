# Generated by Django 3.0.7 on 2020-06-21 02:19

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
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('slug', models.CharField(max_length=250, unique=True)),
                ('short_description', models.TextField(blank=True, max_length=2000, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('created_date', models.DateField(auto_now=True)),
                ('state', models.CharField(choices=[('draft', 'draft'), ('published', 'published'), ('archived', 'archived')], default='draft', max_length=20)),
                ('author', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
