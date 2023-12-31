# Generated by Django 4.1.4 on 2023-08-22 05:05

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('blog', models.TextField()),
                ('image', models.ImageField(upload_to='blogs_images/', verbose_name='Blog Image (370*270)')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique=True)),
                ('created', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': '06. Blogs',
            },
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='blogs_images/', verbose_name='Blog Image (94*125)')),
                ('stars', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': '06. Testimonials',
            },
        ),
        migrations.AlterField(
            model_name='companysetup',
            name='color_logo',
            field=models.ImageField(upload_to='logos', verbose_name='Color Logo (172*43)'),
        ),
        migrations.AlterField(
            model_name='companysetup',
            name='white_logo',
            field=models.ImageField(upload_to='logos', verbose_name='White Logo (172*43)'),
        ),
        migrations.AlterField(
            model_name='homecontent',
            name='header_image',
            field=models.ImageField(upload_to='home_images/', verbose_name='Header Image (557*757)'),
        ),
    ]
