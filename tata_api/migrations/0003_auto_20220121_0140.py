# Generated by Django 3.2.9 on 2022-01-20 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tata_api', '0002_auto_20220119_0229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tata_rec',
            name='Ticket_ID',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='tata_rec',
            name='Zip',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
