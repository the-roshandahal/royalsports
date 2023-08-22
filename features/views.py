from django.shortcuts import render
from .models import *
# Create your views here.


def home(request):
    blogs = Blog.objects.all()[:3]
    testimonials = Testimonial.objects.all()
    sliders = Slider.objects.all()
    partners = Partner.objects.all()
    try:
        home = HomeContent.objects.all()[:1].get()
    except HomeContent.DoesNotExist:
        home = None


    context = {
        'sliders':sliders,
        'home':home,
        'blogs':blogs,
        'testimonials':testimonials,
        'partners':partners,
    }
    return render(request,'index.html',context)