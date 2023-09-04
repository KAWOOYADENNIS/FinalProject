from django.urls import path
#let us reuse the django login view
from django.contrib.auth import views as auth_views

#lets import views file from 'spareapp' application
from spareapp import views
urlpatterns = [
    path('', views.mainpage, name= 'mainpage'),
   
    #path for login
    path('login_details/',auth_views.LoginView.as_view(template_name='dennis/login_details.html'),name='login_details'),
    path('home_details/',views.home_details,name='home_details'),
    path('about_details/',views.about_details,name='about_details'),
    path('logout/',auth_views.LogoutView.as_view(template_name='dennis/mainpage.html'),name='logout'),
    
    
    #path to home details
    path('home_details/<int:product_id>',views.product_detail, name= 'product_detail'),
    
    
    #this handles the receipt path after the sale
    path('receipt/',views.receipt, name= 'receipt'),
    path('receipt/<int:receipt_id>',views.receipt_detail,name='receipt_detail'),
    
    #this handles the sales path
    path('all_sales/',views.all_sales, name= 'all_sales'),
    path('issue_item/<str:pk>',views.issue_item, name= 'issue_item'),
    
    #add to stock path
    path('add_to_stock/<str:pk>',views.add_to_stock, name= 'add_to_stock'),
]