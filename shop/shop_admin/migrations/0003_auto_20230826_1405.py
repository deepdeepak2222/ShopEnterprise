# Generated by Django 3.2.20 on 2023-08-26 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop_admin', '0002_auto_20230724_0457'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransactionDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('transaction_date', models.DateTimeField()),
                ('total_money', models.FloatField()),
                ('transaction_detail', models.CharField(blank=True, max_length=500, null=True)),
                ('transaction_type', models.PositiveSmallIntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='duepayment',
            name='due',
        ),
        migrations.RemoveField(
            model_name='due',
            name='due_history',
        ),
        migrations.RemoveField(
            model_name='due',
            name='payment_history',
        ),
        migrations.DeleteModel(
            name='DueDetail',
        ),
        migrations.DeleteModel(
            name='DuePayment',
        ),
        migrations.AddField(
            model_name='transactiondetail',
            name='due',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='due_of_due_history', to='shop_admin.due'),
        ),
        migrations.AddField(
            model_name='due',
            name='transaction_history',
            field=models.ManyToManyField(related_name='due_of_transaction', to='shop_admin.TransactionDetail'),
        ),
    ]
