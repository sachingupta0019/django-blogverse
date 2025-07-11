# Generated by Django 5.2.3 on 2025-07-02 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=128)),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=64)),
                ('phone', models.CharField(max_length=10)),
                ('gender', models.CharField(choices=[('Male', 'M'), ('Female', 'F'), ('Other', 'Other')], max_length=6)),
                ('address', models.TextField()),
                ('photo', models.ImageField(upload_to='user/profile/')),
            ],
        ),
    ]
