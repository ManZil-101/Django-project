# Generated by Django 3.2 on 2022-02-04 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sahakari_app', '0003_account_info_account_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account_info',
            name='citizenship_no',
            field=models.IntegerField(blank=b'I01\n', null=b'I01\n'),
        ),
        migrations.AlterField(
            model_name='account_info',
            name='images_fields',
            field=models.ImageField(null=b'I01\n', upload_to='images/'),
        ),
    ]
