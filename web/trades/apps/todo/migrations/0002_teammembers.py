# Generated by Django 2.1.10 on 2020-11-15 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamMembers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.TextField(max_length=50)),
                ('last_name', models.TextField(max_length=50)),
                ('image', models.ImageField(default='todo/unknown.png', upload_to='todo/')),
            ],
        ),
    ]
