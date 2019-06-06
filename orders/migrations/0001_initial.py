# Generated by Django 2.1.5 on 2019-05-21 18:25

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('description', models.CharField(max_length=450)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField()),
                ('location', models.DecimalField(decimal_places=2, max_digits=30)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=11)),
                ('user_ranking', models.SmallIntegerField()),
                ('company_ranking', models.SmallIntegerField()),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Profile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('price', models.DecimalField(decimal_places=10, max_digits=30)),
                ('description', django.contrib.postgres.fields.jsonb.JSONField()),
                ('status', models.BooleanField()),
                ('picture', models.ImageField(blank=True, null=True, upload_to='product/pictures')),
            ],
        ),
        migrations.CreateModel(
            name='Product_Has_Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.SmallIntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Profile_company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('telephone', models.CharField(max_length=45)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='company/pictures')),
                ('location', models.DecimalField(decimal_places=10, max_digits=19)),
                ('rfc', models.CharField(max_length=15)),
                ('addres', models.CharField(max_length=250)),
                ('is_active', models.BooleanField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='profile_company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Profile_company'),
        ),
    ]
