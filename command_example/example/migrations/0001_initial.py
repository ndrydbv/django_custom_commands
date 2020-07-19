# Generated by Django 3.0.8 on 2020-07-19 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('NA', 'North America'), ('EU', 'Europe')], max_length=20)),
                ('region', models.CharField(max_length=2)),
                ('moderator', models.BooleanField()),
            ],
        ),
    ]