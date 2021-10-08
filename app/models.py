from django.db import models

from django.contrib.auth import get_user_model

# Create your models here.
class User(models.Model):
    Email = models.EmailField(max_length=50)
    Password = models.CharField(max_length=50)
    ConfirmPassword = models.CharField(max_length=50,default="abc")
    Role = models.CharField(max_length=50)
    OTP=models.BigIntegerField(default=123)
    is_created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    is_updated = models.DateTimeField(auto_now_add=True)


class Owner(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    Firstname = models.CharField(max_length=50,default="abc")
    Lastname = models.CharField(max_length=50,default="abc")
    Address = models.CharField(max_length=50)
    City = models.CharField(max_length=50,default="abc")
    State = models.CharField(max_length=50,default="abc")
    Gender = models.CharField(max_length=50,default="abc")
    Contact = models.BigIntegerField(default="123")
    DOB = models.CharField(max_length=50,default="2019-11-11")
    



class Customer(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    Firstname = models.CharField(max_length=50,default="abc")
    Lastname = models.CharField(max_length=50,default="abc")
    Contact = models.BigIntegerField(default="123")
    State = models.CharField(max_length=50,default="abc")
    City = models.CharField(max_length=50,default="abc")
    DOB = models.CharField(max_length=50,default="2019-11-11")
    Gender = models.CharField(max_length=50,default="abc")
    Address = models.CharField(max_length=50,default="abc")


class House(models.Model):
    user_id = models.ForeignKey(Owner,on_delete=models.CASCADE)
    Address=models.CharField(max_length=50,default="abc")
    State = models.CharField(max_length=50,default="abc")
    City = models.CharField(max_length=50,default="abc")
    Image=models.ImageField(upload_to="imag/")
    Image1=models.ImageField(upload_to="imag/")
    Image2=models.ImageField(upload_to="imag/")
    Roomno=models.CharField(max_length=50,default="abc")
    Rent=models.CharField(max_length=50,default="1000")
    AC=models.CharField(max_length=50,default="abc")
    Gender=models.CharField(max_length=50,default="abc")
    Speciality=models.CharField(max_length=500,default="abc")
    Food=models.CharField(max_length=50,default="abc")
    Status=models.BigIntegerField(default=0)

class Cart(models.Model):
    user_id = models.ForeignKey(Customer,on_delete=models.CASCADE)
    user_id2 = models.ForeignKey(House,on_delete=models.CASCADE)
    Address=models.CharField(max_length=50,default="abc")
    Image=models.ImageField(upload_to="imag/")
    Roomno=models.CharField(max_length=50,default="abc")
    Rent=models.CharField(max_length=50,default="abc")


class Transaction(models.Model):
    made_by = models.ForeignKey(User, related_name='transactions', 
                                on_delete=models.CASCADE)
    made_on = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()
    order_id = models.CharField(unique=True, max_length=100, null=True, blank=True)
    checksum = models.CharField(max_length=100, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.order_id is None and self.made_on and self.id:
            self.order_id = self.made_on.strftime('PAY2ME%Y%m%dODR') + str(self.id)
        return super().save(*args, **kwargs)


    



    