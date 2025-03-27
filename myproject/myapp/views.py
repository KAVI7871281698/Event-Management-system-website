from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from django.conf import settings
from django.contrib import messages
from .models import register_table,cateringservice,package,order,reviews
# from .models import register_page,products,add_to_cart,Ordernow
import os
# import datetime
# from functools import wraps
# from django.db.models import Sum 
# Create your views here.

# Create your views here.

def home(request):
    return render(request,'home.html')

def register(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        address=request.POST['address']
        mobile = request.POST['phone']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']

    
        if password!=confirm_password:
            messages.error(request,'Password does not match')
            return redirect('register')
        
        
        if register_table.objects.filter(email=email).exists():
            messages.error(request,'Email already exits')
            return redirect('login')
        data_store = register_table(name=name,email=email,password=password,address=address,mobile=mobile)
        data_store.save()
        messages.success(request,'Regiester Successfully')
        return redirect('login')
    
    return render(request,'register.html')

def login(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']

        try:
            take_data=register_table.objects.get(email=email)
            if take_data.password==password:
                request.session['email']=email
                request.session['name']=take_data.name
                request.session['is_logged_in']=True
                return redirect('index')
            else:
                messages.error(request,'Incorrect Password')
        except:
            messages.error(request,'Incorrect Email')

    return render(request,'login.html')

def logout(request):
    request.session.flush()
    return redirect('login')

def services(request):
    if request.method == 'POST':
        # Retrieve name and email from session
        name = request.session.get('name')
        email = request.session.get('email')
        
        catering_package = request.POST.get('Catering')
        catering_type = request.POST.get('Veg(or)Non-veg')
        event_date = request.POST.get('date')
        description = request.POST.get('Descrpion')

        # Save data to the database
        catering_service = cateringservice(
            name=name,
            email=email,
            catering_package=catering_package,
            catering_type=catering_type,
            event_date=event_date,
            description=description
        )
        catering_service.save()
        
        return redirect('booking_page')
    
    return render(request,'services.html')

def booking_page(request):
    return render(request,'booking_page.html')

def index(request):
    return render(request,'index.html')

def my_booking(request):
    # Retrieve name and email from session
    name = request.session.get('name')
    email = request.session.get('email')
    
    # Retrieve data from the database
    my_booking = order.objects.filter(name=name,email=email)
    
    return render(request,'my_booking.html',{'bookings':my_booking})

def decoration(request):
    plans = package.objects.filter(category='decoration')
    return render(request,'decoration.html',{'planes':plans})

def photography(request):
    plans = package.objects.filter(category='photography')
    return render(request,'photography.html',{'planes':plans})

def beauty(request):
    plans = package.objects.filter(category='beauty')
    return render(request,'beauty.html',{'planes':plans})

def catering(request):
    plans = package.objects.filter(category='catering')
    return render(request,'catering.html',{'planes':plans})

def booked(request,id):
    name = request.session.get('name')
    email = request.session.get('email')
    order_details = get_object_or_404(package,id=id)
    return render(request,'booked.html',{'orders':order_details,'name':name,'email':email})

def confirm_order(request,id):
    if request.method == 'POST':
        location = request.POST['address']
        event_date = request.POST['date']
        orders = package.objects.get(id=id)
        name = request.session.get('name')
        email = request.session.get('email')
        plans = orders.package_name
        features = orders.features
        store = order(location=location,event_date=event_date,name=name,email=email,plans=plans,features=features,event=orders)
        store.save()
    view = order.objects.filter(email=email).last()
    return render(request,'confirm_order.html',{'show':view})

def review(request):
    if request.method == 'POST':
        name = request.POST['name']
        review = request.POST['review']
        store = reviews(name=name,reviews=review)
        store.save()
    return render(request,'reviews.html')

def dashboard(request):
    total_user = register_table.objects.count() 
    total_orders = order.objects.count() #Number of Product on sale
    total_reviews = reviews.objects.count()
    total_event = package.objects.count()
    return render(request,'dashboard.html',{'total_review':total_reviews,'total_orders':total_orders,'total_customer':total_user,'total_event':total_event})

def dashboard_customer(request):
    customer = register_table.objects.all()
    return render(request,'dashboard_customer.html',{'see':customer})

def dashboard_event(request):
    product = package.objects.all()
    return render(request,'dashboard_event.html',{'product_items':product})

def order_dashboard(request):
    orders = order.objects.all()
    return render(request,'order_dashboard.html',{'order_item':orders})

def dashboard_review(request):
    review = reviews.objects.all()
    return render(request,'dashboard_review.html',{'review_item':review})

def logout2(request):
    request.session.flush()
    return redirect('index')


