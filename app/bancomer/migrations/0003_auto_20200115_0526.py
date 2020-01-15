# Generated by Django 3.0.2 on 2020-01-15 05:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bancomer', '0002_auto_20200115_0332'),
    ]

    operations = [
        migrations.CreateModel(
            name='Summary',
            fields=[
            ],
            options={
                'verbose_name': 'Summary',
                'verbose_name_plural': 'Summary',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('bancomer.transaction',),
        ),
        migrations.AlterUniqueTogether(
            name='transaction',
            unique_together={('applied', 'description', 'amount')},
        ),
    ]