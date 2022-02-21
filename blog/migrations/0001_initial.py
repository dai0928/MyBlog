# Generated by Django 3.2.6 on 2022-02-19 14:23

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CreateBlogModel',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('32a62db6-fd54-4c1c-85d9-701de2c4080c'), editable=False, primary_key=True, serialize=False)),
                ('blog_title', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='作成日時')),
                ('updated_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='更新日時')),
                ('user', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
