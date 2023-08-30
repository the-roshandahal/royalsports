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
    image = models.ImageField(upload_to="slider_images/desktop",verbose_name="Image (1920*1080)")
    mobile_image = models.ImageField(upload_to="slider_images/mobile",verbose_name="Mobile Image (450*750)")
    sub_heading_text = models.CharField(max_length=200)
    def __str__(self):
        return self.sub_heading_text
    class Meta:
        verbose_name_plural = "03. Banner Image" 



class Blog(models.Model):
    title = models.CharField(max_length=200)
    blog = models.TextField()
    image = models.ImageField(upload_to="blogs_images/",verbose_name="Blog Image (370*270)")
    slug = AutoSlugField(populate_from='title', unique=True)
    created = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "04. Blogs" 




class Testimonial(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    testimonial = models.TextField()

    image = models.ImageField(upload_to="testimonial_images/",verbose_name="Testimonial Image (94*125)")
    stars = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "05. Testimonials" 


class Partner(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="partner_images/",verbose_name="Partner Image (94*125)")
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "06. Partner" 




class Contact(models.Model):
    name = models.TextField()
    email = models.TextField()
    contact = models.TextField()
    subject = models.TextField(null=True, blank=True)
    message = models.TextField()
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "07. Contact"



class JoinRcs(models.Model):
    data_set = models.CharField(max_length=200)
    heading_image = models.ImageField(upload_to="join_images/",verbose_name="Heading Image (1920*800)")
    court_image = models.ImageField(upload_to="join_images/",verbose_name="Court Image (1920*800)")
    booking_details1 = models.TextField()
    booking_details2 = models.TextField()
    bottom_text = models.TextField()
    
    def __str__(self):
        return self.data_set
    class Meta:
        verbose_name_plural = "08. Join RCS Page Content" 


class Participation(models.Model):
    title = models.CharField(max_length=255)
    court_image = models.ImageField(upload_to="join_images/",verbose_name="Featured Image (570*400)")
    description = models.TextField()
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "09. Participation and Honours" 



class Gallery(models.Model):
    title = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "10. Gallery" 

class GalleryImage(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='gallery_images/',verbose_name="Heading Image (370*307)")
    
    def __str__(self):
        return f"Image in {self.gallery.title}"
    



class Event(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="join_images/",verbose_name="Featured Image (954*774)")
    description = models.TextField()
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "11. Events" 