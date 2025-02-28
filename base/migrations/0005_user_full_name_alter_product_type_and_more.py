# Generated by Django 5.1.2 on 2024-10-19 02:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_user_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='full_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.producttype'),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.product'),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='vendor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.vendor'),
        ),
        migrations.AlterField(
            model_name='sales',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.customer'),
        ),
        migrations.AlterField(
            model_name='sales',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.product'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default='username', max_length=255),
        ),
    ]
