# Generated by Django 4.0.2 on 2022-02-18 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('second_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='num_stars',
            field=models.IntegerField(choices=[(1, 'Worst'), (2, 'Not Good'), (3, 'Bad'), (4, 'Good'), (5, 'Excellent')]),
        ),
    ]
