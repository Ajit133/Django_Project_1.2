# Generated by Django 4.0.2 on 2022-02-18 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Musician',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('instrument', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('release_data', models.DateField()),
                ('num_stars', models.IntegerField(verbose_name=((1, 'Worst'), (2, 'Not Good'), (3, 'Bad'), (4, 'Good'), (5, 'Excellent')))),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='second_app.musician')),
            ],
        ),
    ]
