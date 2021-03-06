# Generated by Django 3.2.6 on 2022-02-20 07:49

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20220220_1647'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='createblogmodel',
            name='create_user',
        ),
        migrations.AddField(
            model_name='createblogmodel',
            name='user',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='createblogmodel',
            name='id',
            field=models.UUIDField(default=uuid.UUID('0370f889-73c0-491e-9972-9fc747c04347'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
