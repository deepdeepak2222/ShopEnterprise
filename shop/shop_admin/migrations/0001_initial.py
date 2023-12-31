# Generated by Django 4.2.1 on 2023-06-08 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Due',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('f_name', models.CharField(max_length=50)),
                ('l_name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=15)),
                ('total_money', models.FloatField()),
                ('payment_history', models.JSONField(default=dict)),
                ('remaining_money', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
