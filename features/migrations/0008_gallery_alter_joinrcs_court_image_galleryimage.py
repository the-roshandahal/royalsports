# Generated by Django 4.1.4 on 2023-08-22 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0007_joinrcs'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='joinrcs',
            name='court_image',
            field=models.ImageField(upload_to='join_images/', verbose_name='Court Image (1920*800)'),
        ),
        migrations.CreateModel(
            name='GalleryImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='gallery_images/')),
                ('gallery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='features.gallery')),
            ],
        ),
    ]
