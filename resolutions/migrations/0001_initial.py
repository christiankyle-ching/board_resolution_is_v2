# Generated by Django 4.0.3 on 2022-04-04 08:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(db_index=True, default=True, editable=False)),
                ('deleted_at', models.DateTimeField(default=None, editable=False, null=True)),
                ('added_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('added_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Resolution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(db_index=True, default=True, editable=False)),
                ('deleted_at', models.DateTimeField(default=None, editable=False, null=True)),
                ('number', models.CharField(max_length=50)),
                ('title', models.TextField()),
                ('certificate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resolutions.certificate')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CertificateImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(db_index=True, default=True, editable=False)),
                ('deleted_at', models.DateTimeField(default=None, editable=False, null=True)),
                ('image', models.ImageField(upload_to='certificates/')),
                ('certificate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resolutions.certificate')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
