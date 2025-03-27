from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('services',views.services,name='services'),
    path('booking_page',views.booking_page,name='booking_page'),
    path('index',views.index,name='index'),
    path('my_booking',views.my_booking,name='my_booking'),
    path('logout',views.logout,name='logout'),
    path('decoration',views.decoration,name='decoration'),
    path('photography',views.photography,name='photography'),
    path('beauty',views.beauty,name='beauty'),
    path('catering',views.catering,name='catering'),
    path('booked/<int:id>/',views.booked,name='booked'),
    path('confirm_order/<int:id>/',views.confirm_order,name='confirm_order'),
    path('reviews',views.review,name='reviews'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('dashboard_customer',views.dashboard_customer,name='dashboard_customer'),
    path('dashboard_event',views.dashboard_event,name='dashboard_event'),
    path('order_dashboard',views.order_dashboard,name='order_dashboard'),
    path('dashboard_review',views.dashboard_review,name='dashboard_review'),
    path('logout2',views.logout2,name='logout2'),
]
