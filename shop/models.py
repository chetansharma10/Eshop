from django.db import models

# Create your models here.
class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    desc=models.CharField(max_length=50)
    category=models.CharField(max_length=50,default="")
    subcategory=models.CharField(max_length=50,default="")
    price=models.IntegerField(default=0)
    image=models.ImageField(upload_to="shop/imgs",default="")
    pub_date=models.DateField()

    def __str__(self):
        return self.product_name

class Accounts(models.Model):
    acct_id=models.AutoField
    acc_fname=models.CharField(max_length=50)
    acc_lname=models.CharField(max_length=50)
    acc_email=models.EmailField(max_length=50)
    acc_pass1=models.CharField(max_length=50)
    acc_pass2=models.CharField(max_length=50)

    def __str__(self):
        return self.acc_fname

class CheckDetails(models.Model):
    user_mail=models.CharField(max_length=50)
    quantity=models.IntegerField(default=0)
    subQuantity=models.IntegerField(default=0)
    price=models.IntegerField(default=0)
    def __str__(self):
        return self.user_mail






        