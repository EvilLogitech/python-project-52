# Generated by Django 4.2.7 on 2023-12-02 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statuses', '0003_alter_status_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='Имя'),
        ),
    ]
