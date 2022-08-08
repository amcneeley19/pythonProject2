# Generated by Django 4.1 on 2022-08-07 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurant_name', models.CharField(max_length=20)),
                ('health_value', models.IntegerField(default=0)),
                ('alcohol', models.BooleanField(default=False)),
                ('image', models.ImageField(upload_to='')),
                ('distance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
