from django.shortcuts import render,redirect
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