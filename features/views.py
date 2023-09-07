from django.contrib import messages
from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from django.conf import settings
import requests
# Create your views here.


def home(request):
    blogs = Blog.objects.all()[:3]
    testimonials = Testimonial.objects.filter(active=True)
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


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        contact = request.POST['contact']
        subject = request.POST['subject']
        message = request.POST['message']
        contact_obj = Contact.objects.create( name=name,email=email,contact=contact,subject=subject,message=message)
        contact_obj.save()
        return redirect('contact')
    else:
        return render(request,'contact_us.html')

def join_rsc(request):
    try:
        rcs = JoinRcs.objects.all()[:1].get()
    except JoinRcs.DoesNotExist:
        rcs = None
    
    context = {
        'rcs':rcs
    }
    return render(request,'join_rsc.html',context)


def gallery(request):
    gallerys = Gallery.objects.all()
    context = {
        'gallerys':gallerys
    }
    return render(request,'gallery.html',context)


def gallery_details(request,id):
    gallery = Gallery.objects.get(id=id)
    context = {
        'gallery':gallery
    }
    return render(request,'gallery_details.html',context)


def participation(request):
    participations = Participation.objects.all()
    context = {
        'participations':participations
    }
    return render(request,'participation.html',context)


def events(request):
    events = Event.objects.all().order_by('-id')
    context = {
        'events':events
    }
    return render(request,'events.html',context)






def add_review(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        title = request.POST.get('title')
        testimonial = request.POST.get('testimonial')
        recaptcha_response = request.POST.get('g-recaptcha-response')
        stars = request.POST.get('stars')
        image = request.FILES['image']
        stars = int(stars)
        recaptcha_valid = validate_recaptcha(recaptcha_response)
        if not recaptcha_valid:
            messages.info(request, "Invalid Captcha. Please Try Again!")
            return redirect('add_review')


        if not (name and title and testimonial and image and stars):
            messages.info(request, "Please fill out all fields.")
            return redirect('add_review')

        Testimonial.objects.create(
            name=name,
            title=title,
            testimonial=testimonial,
            stars=stars,
            image=image,
        )
        messages.info(request, "Testimonial submitted for admin's approval. Thank you!")
        return redirect('join_rsc')
    else:
        recaptcha_site_key = settings.RECAPTCHA_SITE_KEY
        context = {
            'recaptcha_site_key':recaptcha_site_key
        }
        return render(request, 'add_review.html',context)

def validate_recaptcha(recaptcha_response):
    if not recaptcha_response:
        return False

    payload = {
        'secret': settings.RECAPTCHA_SECRET_KEY,
        'response': recaptcha_response,
    }

    response = requests.post('https://www.google.com/recaptcha/api/siteverify', data=payload)
    result = response.json()

    return result.get('success', False)
