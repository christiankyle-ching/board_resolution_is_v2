# Generated by Django 4.0.4 on 2022-05-05 01:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('resolutions', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='certificateimage',
            options={'ordering': ['image']},
        ),
        migrations.AddField(
            model_name='resolution',
            name='added_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]