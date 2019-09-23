# Generated by Django 2.2.5 on 2019-09-23 06:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='story',
        ),
        migrations.AddField(
            model_name='blog',
            name='body',
            field=models.CharField(default='', max_length=400),
        ),
        migrations.AddField(
            model_name='blog',
            name='date_published',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='title',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
