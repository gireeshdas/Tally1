# Generated by Django 4.1 on 2023-09-06 07:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0011_purchase_voucher_purchase_particulars'),
    ]

    operations = [
        migrations.AddField(
            model_name='contra_voucher',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.companies'),
        ),
    ]
