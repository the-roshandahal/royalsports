# Generated by Django 4.1.4 on 2023-08-22 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0004_alter_testimonial_stars'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='blogs_images/', verbose_name='Blog Image (94*125)')),
            ],
            options={
                'verbose_name_plural': '06. Partner',
            },
        ),
    ]
