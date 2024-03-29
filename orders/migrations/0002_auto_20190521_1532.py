# Generated by Django 2.1.5 on 2019-05-21 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='name',
            new_name='product_name',
        ),
        migrations.RenameField(
            model_name='profile_company',
            old_name='full_name',
            new_name='company_name',
        ),
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.AlterField(
            model_name='profile_company',
            name='rfc',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='profile_company',
            name='telephone',
            field=models.CharField(max_length=10),
        ),
    ]
