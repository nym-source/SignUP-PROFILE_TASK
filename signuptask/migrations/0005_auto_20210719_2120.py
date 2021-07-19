# Generated by Django 3.1.7 on 2021-07-19 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signuptask', '0004_auto_20210719_2116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='birth_date',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='location',
        ),
        migrations.AddField(
            model_name='profile',
            name='Full_Address',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='pincode',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_PIC',
            field=models.FileField(blank=True, upload_to='user_images/'),
        ),
        migrations.AddField(
            model_name='profile',
            name='state',
            field=models.CharField(max_length=200, null=True),
        ),
    ]