# Generated by Django 4.0.3 on 2022-05-15 02:41

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
            name='product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(default='NULL', max_length=30)),
                ('price', models.FloatField(default='NULL')),
                ('brand', models.CharField(default='NULL', max_length=30)),
                ('model', models.CharField(default='NULL', max_length=50)),
                ('type', models.CharField(default='NULL', max_length=50)),
                ('date', models.DateField(default='0000-00-00')),
                ('invoice_image', models.ImageField(default='NULL', upload_to='')),
                ('Warranty', models.BooleanField(default='NULL')),
                ('duration_warranty', models.IntegerField(default='NULL')),
                ('Is_Alert_Needed', models.BooleanField(default='NULL')),
                ('Insurance', models.BooleanField(default='NULL')),
                ('duration_insurance', models.IntegerField(default='NULL')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('photo', models.ImageField(blank=True, upload_to='users/%Y/%m/%d')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
