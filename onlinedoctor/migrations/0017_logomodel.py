# Generated by Django 3.2.6 on 2021-11-19 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinedoctor', '0016_rename_cityname_customusermodel_citycode'),
    ]

    operations = [
        migrations.CreateModel(
            name='logoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anaLogo', models.ImageField(blank=True, null=True, upload_to='logolar')),
                ('footerLogo', models.ImageField(blank=True, null=True, upload_to='logolar')),
            ],
            options={
                'verbose_name': 'logo',
                'verbose_name_plural': 'logolar',
                'db_table': 'logolar',
            },
        ),
    ]
