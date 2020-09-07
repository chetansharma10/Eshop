from django.urls import path
from . import views
urlpatterns = [

    path("",views.index,name="index"),

    path("contact/",views.contact,name="ContactUs"),
    path("login/",views.login,name="login"),


    path("cart/",views.cart,name="cart"),

  
   
    path("logout/",views.logout,name="logout"),

    path("productView/<int:myid>/",views.productView,name="productView"),
   

]
