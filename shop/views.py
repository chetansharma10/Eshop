from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Product
from .models import Accounts
from .models import CheckDetails
from json import dumps
from django.contrib.auth.hashers import make_password,check_password
# Create your views here.
MAIL=None
def index(request):
    category=request.POST
    show="ALL"
    check="ALL"
    if category.get('MEN')!=None:
        show="MEN"
    elif category.get('WOMEN')!=None:
        show="WOMEN"
    elif category.get('CHILD')!=None:
        show="CHILD"
    elif category.get('ALL')!=None:
        show="ALL"
    else:
        show="ALL"
    allProducts=Product.objects.all()

    showOUT='False'
    if request.session.get('userPresent'):
        showOUT='True'
        email=request.session.get('email')
        param={"product":allProducts,"show":show,"check":check,'showOUT':showOUT,'email':email}

        

    else:
        showOUT='False'
        param={"product":allProducts,"show":show,"check":check,'showOUT':showOUT}
    return render(request,'shop/index.htm',param)





def contact(request):
    may=False
    if(request.method=="POST"):    
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
        email=request.POST.get('email')

        if (fname in email and lname in email) and (pass1==pass2):
            if Accounts.objects.filter(acc_email=email):
                return render(request,'shop/contact.htm',{'error3':"Email Already Exists"})
            else:
                if len(pass1)<8:
                    return render(request,'shop/contact.htm',{'error4':"Weak Password,It must be of at least 8 digits"})
                else:    
                    pass1=make_password(pass1)
                    pass2=make_password(pass2)
                    data=Accounts(acc_fname=fname,acc_lname=lname,acc_email=email,acc_pass1=pass1,acc_pass2=pass2)
                    data.save()
                    return redirect(index)
        elif pass1!=pass2:
            return render(request,'shop/contact.htm',{'error2':"Please Confirm Your Password"})
        else:
            return render(request,'shop/contact.htm',{'error':"First name and Last name be in Email"})
    else:
        return render(request,'shop/contact.htm',{'error1':"Create Your Account"})



def logout(request):
    if request.session.get('userPresent'):
        del request.session['userPresent']
        del request.session['email']
        MAIL=None
    return redirect(index)


def login(request):
    checkEmail=False;checkPassword=False
    if request.method=="POST":    
        email=request.POST.get('email')
        password=request.POST.get('pass')
        
        if len(Accounts.objects.filter(acc_email=email))==1 and Accounts.objects.filter(acc_email=email)!=None:
            checkEmail=True
            data=Accounts.objects.filter(acc_email=email)
            for a in data:
                if check_password(password,a.acc_pass1):
                    checkPassword=True
                    break
                else:
                    checkPassword=False
            if checkEmail==True and checkPassword==True:
                    MAIL=email
                    request.session['userPresent']=True
                    request.session['email']=email
                    return redirect(index)
            else:
                return render(request,'shop/login.htm',{'error2':"Invalid Credentials"})
        else:
            return render(request,'shop/login.htm',{'error3':"Invalid Email"})

    else:
        return render(request,'shop/login.htm',{'error1':"Please Fill your account Details"})




def cart(request):
    error1=""
    error2=""
    if request.session.get('userPresent')==None:
        error1="Please Login in your account"
    else:
        emailId=request.session.get('email')
        quan=request.GET.get('Quantity')
        prices=request.GET.get('Prices')
        subQ=request.GET.get('Subquantity')
        if quan!=None or prices!=None or subQ!=None:    
            if len(quan)==0 or len(prices)==0 or len(subQ)==0:
                error1="You have no products in account"
            else:    
                quan=int(quan)
                prices=int(prices)
                subQ=int(subQ)
                db=CheckDetails(user_mail=emailId,quantity=quan,subQuantity=subQ,price=prices)
                db.save()

                

    products=Product.objects.all()
    data={}
    for i in range(0,len(products)):
        data[i+1]=[products[i].product_name,
                products[i].desc,
                products[i].category,
                products[i].subcategory,
                products[i].price,
                str(products[i].image),
                str(products[i].pub_date) ]        
    dataJson=dumps(data)
    return render(request,'shop/cart.htm',{'data':dataJson,'error1x':error1,'error2x':error2})

def productView(request,myid):
    product_detail=Product.objects.filter(id=myid)
    return render(request,'shop/productView.htm',{'product_detail':product_detail,'id':myid})