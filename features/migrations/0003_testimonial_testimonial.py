# Generated by Django 4.1.4 on 2023-08-22 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0002_blog_testimonial_alter_companysetup_color_logo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonial',
            name='testimonial',
            field=models.TextField(default='sdad sda das'),
            preserve_default=False,
        ),
    ]
