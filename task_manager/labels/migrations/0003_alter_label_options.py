# Generated by Django 4.2.7 on 2023-12-02 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labels', '0002_alter_label_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='label',
            options={'verbose_name': 'Label', 'verbose_name_plural': 'Labels'},
        ),
    ]