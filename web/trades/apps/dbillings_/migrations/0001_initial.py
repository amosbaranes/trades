# Generated by Django 2.1.10 on 2020-11-15 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_number', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50, null=True)),
                ('last_name', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('invoice_number', models.AutoField(primary_key=True, serialize=False)),
                ('invoice_date', models.DateField(auto_now=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbillings.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('unit_price', models.DecimalField(decimal_places=2, default=0, max_digits=11)),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbillings.Invoice')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('item_number', models.AutoField(primary_key=True, serialize=False)),
                ('item_name', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='invoiceitem',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbillings.Item'),
        ),
    ]
