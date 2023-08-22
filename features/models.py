from django.core.validators import MaxValueValidator, MinValueValidator
from autoslug import AutoSlugField
from django.db import models
from django.contrib.auth.models import User

class CompanySetup(models.Model):
    data_set = models.CharField(max_length=200)
    color_logo = models.ImageField(upload_to="logos",verbose_name="Color Logo (172*43)")
    white_logo = models.ImageField(upload_to="logos",verbose_name="White Logo (172*43)")

    company_name = models.CharField(max_length=255)

    location = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)
    opening_hours = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    
    facebook_url = models.URLField(null=True,blank=True)
    instagram_url = models.URLField(null=True,blank=True)
    youtube_url = models.URLField(null=True,blank=True)

    created = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.data_set
    class Meta:
        verbose_name_plural = "01. Company Setup" 





class HomeContent(models.Model):
    data_set = models.CharField(max_length=200)

    header_text = models.TextField()
    header_image = models.ImageField(upload_to="home_images/", verbose_name="Header Image (557*757)")

    mission = models.TextField()
    vision = models.TextField()

    def __str__(self):
        return self.data_set
    class Meta:
        verbose_name_plural = "02.Home Page Content" 
        

class Slider(models.Model):
    image = models.ImageField(upload_to="slider_images",verbose_name="Image (1920*1080)")
    heading_text = models.CharField(max_length=200) 
    sub_heading_text = models.CharField(max_length=200) 
    button_text = models.CharField(max_length=50)
    button_url = models.URLField()
    def __str__(self):
        return self.heading_text
    class Meta:
        verbose_name_plural = "04. Slider" 



class Blog(models.Model):
    title = models.CharField(max_length=200)
    blog = models.TextField()
    image = models.ImageField(upload_to="blogs_images/",verbose_name="Blog Image (370*270)")
    slug = AutoSlugField(populate_from='title', unique=True)
    created = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "06. Blogs" 




class Testimonial(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    testimonial = models.TextField()

    image = models.ImageField(upload_to="testimonial_images/",verbose_name="Testimonial Image (94*125)")
    stars = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "06. Testimonials" 


class Partner(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="partner_images/",verbose_name="Partner Image (94*125)")
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "06. Partner" 