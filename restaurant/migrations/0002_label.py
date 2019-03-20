# Generated by Django 2.1.7 on 2019-03-20 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Label',
            fields=[
                ('Label_Name', models.CharField(max_length=20)),
                ('Label_Id', models.AutoField(primary_key=True, serialize=False)),
                ('Label_Menu_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.Menu')),
            ],
        ),
    ]
