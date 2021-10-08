from django.shortcuts import render,HttpResponseRedirect,reverse,redirect
from.models import*
from random import*
from .utils import*

from django.contrib.auth import authenticate, login as auth_login
from django.conf import settings
from .models import Transaction
from .paytm import generate_checksum, verify_checksum

from django.views.decorators.csrf import csrf_exempt
#from .models import Transaction
#from .paytm import generate_checksum, verify_checksum

#from django.views.decorators.csrf import csrf_exempt
#from .utils import*

# Create your views here.

def indexpage(request):
    return render(request,"app/index.html")


def ownerindexpage(request):
    return render(request,"owner/index.html")


def HouseFormPage(request):
    return render(request,"owner/form1.html")

def RegisterPage(request):
    return render(request,"app/register.html")

def LoginPage(request):
    return render(request,"app/login.html")


def RegisterUser(request):
    try:
        if request.POST['role']=="Owner":
            print("==========================GOT Owner ROLE")
            role=request.POST['role']
            email=request.POST['email']
            password=request.POST['password']
            cpassword=request.POST['cpassword']
            fname=request.POST['fname']
            lname=request.POST['lname']
            contact=request.POST['contact']
            user=User.objects.filter(Email=email)
            if user:
                message="User Already Exist"
                return render(request,"app/register.html",{'message':message})
            else:
                if password==cpassword:
                    newuser=User.objects.create(Email=email,Password=password,Role=role)
                    newseller=Owner.objects.create(user_id=newuser,Firstname=fname,Lastname=lname,Contact=contact)
                    print("REGISTRATION COMPLETED")
                    return render(request,"app/login.html")

                else:
                    message="Password does not match with confirm password"
                    return render(request,"app/register.html",{'message':message})


        else:
            role=request.POST['role']
            email=request.POST['email']
            password=request.POST['password']
            cpassword=request.POST['cpassword']
            fname=request.POST['fname']
            lname=request.POST['lname']
            contact=request.POST['contact']
        
            user=User.objects.filter(Email=email)
            if user:
                message="User Already Exist"
                return render(request,"app/register.html",{'message':message})
            else:
                    if password==cpassword:
                        otp = randint(1000, 9999)
                        newuser=User.objects.create(Email=email,Password=password,Role=role,OTP=otp)
                        newcustomer=Customer.objects.create(user_id=newuser,Firstname=fname,Lastname=lname,Contact=contact)
                        
                        email_subject = "This is your new OTP"
                
                        sendmail(email_subject, 'mail_template', email, {'otp': otp})
                        return render(request,"app/verify.html",{'user':newuser})
                    

               
                    else:
                        message="Password does not match with confirm password"
                        return render(request,"app/register.html",{'message':message})
    except Exception as e1:
            print("Edit Exception    ",e1)


def verify(request,otp):

    otp1=request.POST['otp']
    a=otp==int(otp1)
    print(a)
    
            
    if otp==int(otp1) :
                        print('hello ')
        
                
                        user.save()
    else:
                        message='Wrong OTP'

    

def LoginUser(request):
    if request.POST['role']=="Owner":
        print('=========1=========')
        email=request.POST['email']
        password=request.POST['password']
        user=User.objects.get(Email=email)
        if user:
            print('=========2=========GOT USER')
            if user.Password==password and user.Role=="Owner":
                owner = Owner.objects.get(user_id=user) 
                request.session['id']=user.id
                request.session['Email']=user.Email
                request.session['Role']=user.Role
                request.session['Firstname']=owner.Firstname
                return render(request,"owner/index.html")

                    
            else:
                msg="Password and Role Does not match"
                return render(request,"app/login.html",{'msg':msg})
        else:
                msg="User Does Not match"
                return render(request,"app/login.html",{'msg':msg})


    else:
        email=request.POST['email']
        password=request.POST['password']
        user=User.objects.get(Email=email)

        if user:
            if user.Password==password and user.Role=="Customer":
                customer=Customer.objects.get(user_id=user) 
                request.session['id']=user.id
                request.session['Email']=user.Email
                request.session['Role']=user.Role
                request.session['Firstname']=customer.Firstname
        
                return render(request,"app/index-1.html")
            else:
                msg="Password and Role Does nor match"
                return render(request,"app/login.html",{'msg':msg})
        else:
                msg="User Does Not match"
                return render(request,"app/login.html",{'msg':msg})






def AddHouse(request,pk):
    udata = User.objects.get(id=pk)
    if udata.Role=="Owner":
        address=request.POST['address']
        image=request.FILES['image']
        image1=request.FILES['image1']
        image2=request.FILES['image2']
        state=request.POST['state']
        city=request.POST['city']
        roomno=request.POST['roomno']
        rent=request.POST['rent']
        ac=request.POST['ac']
        gender=request.POST['gender']
        speciality=request.POST['speciality']
        food=request.POST['food']
        user=Owner.objects.get(user_id=udata)
        newhouse=House.objects.create(user_id=user,Address=address,Image=image,Image1=image1,Image2=image2,State=state,City=city,Roomno=roomno,Rent=rent,AC=ac,Gender=gender,Speciality=speciality,Food=food)
        msg = "House Add Successfully"
        return render(request,"owner/form1.html",{'msg':msg})




def ShowProfile(request,pk):
    user=User.objects.get(id=pk)
    if user.Role=="Owner":
        ownerdata=Owner.objects.get(user_id=user)
        return render(request,"owner/profile.html",{'key1':ownerdata})
    else:
        customerdata=Customer.objects.get(user_id=user)
        return render(request,"app/dashboard.html",{'key1':customerdata})

def UpdateData(request,pk):
    user=User.objects.get(id=pk)
    if user.Role=="Owner":
        udata=Owner.objects.get(user_id=user)
        udata.Firstname=request.POST['fname']
        udata.Lastname=request.POST['lname']
        udata.City=request.POST['city']
        udata.State=request.POST['state']
        udata.Gender=request.POST['gender']
        udata.Contact=request.POST['contact']
        udata.DOB=request.POST['dob']
        udata.Address=request.POST['address']
        udata.save()
        url=f"/showprofile/{pk}"
        return redirect(url)
    else:
        udata=Customer.objects.get(user_id=user)
        udata.Firstname=request.POST['fname']
        udata.Lastname=request.POST['lname']
        udata.City=request.POST['city']
        udata.State=request.POST['state']
        udata.Gender=request.POST['gender']
        udata.Contact=request.POST['contact']
        udata.DOB=request.POST['dob']
        udata.Address=request.POST['address']
        
        udata.save()
        url=f"/showprofile/{pk}"
        return redirect(url)

def OpenCategory(request,name):
    all_house=House.objects.all().filter(Roomno=name).filter(Status=1)
    return render(request,"app/category-list.html",{'all':all_house})

def OpenCategorylocation(request,name):
    all_house=House.objects.all().filter(City=name).filter(Status=1)
    return render(request,"app/category-list.html",{'all':all_house})

def OpenCategoryforprice(request,price):

    all_house=House.objects.all().filter(Rent__lte=int(price)).order_by('-Rent').filter(Status=1)
    return render(request,"app/category-list.html",{'all':all_house})

def OpenCategory1(request,name):
    all_house=House.objects.all().filter(Roomno=name).filter(Status=1)
    return render(request,"app/category-list1.html",{'all':all_house})

def OpenCategorylocation1(request,name):
    all_house=House.objects.all().filter(City=name).filter(Status=1)
    return render(request,"app/category-list1.html",{'all':all_house})

def OpenCategoryforprice1(request,price):

    all_house=House.objects.all().filter(Rent__lte=int(price)).order_by('-Rent').filter(Status=1)
    return render(request,"app/category-list1.html",{'all':all_house})


def showhousedetail(request,pk):
    all_data=House.objects.get(id=pk)
    
    return render(request,"app/product.html",{'key2':all_data})

def showhousedetail1(request,pk):
    all_data=House.objects.get(id=pk)
    
    return render(request,"app/product1.html",{'key2':all_data})


def getAllHouse(request):
    udata = User.objects.get(id=request.session['id'])
    if udata.Role=="Owner":
        sell = Owner.objects.get(user_id=udata)
        all_data1=House.objects.all().filter(user_id=sell)
        return render(request,"owner/showproducts.html",{'key3':all_data1})


def EditDataById(request,pk):
    edata=House.objects.get(id=pk)
    return render(request,"owner/editproduct.html",{'key4':edata})

def UpdateHouse(request,pk):
    udata=House.objects.get(id=pk)
    udata.Address=request.POST['address']
    udata.State=request.POST['state']
    udata.City=request.POST['city']
    udata.Image=request.POST['image']
    udata.Image1=request.POST['image1']
    udata.Image2=request.POST['image2']
    udata.Roomno=request.POST['roomno']
    udata.Rent=request.POST['rent']
    udata.Ac=request.POST['ac']
    udata.Gender=request.POST['gender']
    udata.Speciality=request.POST['speciality']
    udata.Food=request.POST['food']
    udata.save()
    url=f"/edithouse/{pk}"
    return redirect(url)


def DeleteHouse(request,pk):
    ddata=House.objects.get(id=pk)
    ddata.delete()
    url=f"allhouse/"
    return redirect(url)

def addtoCart(request,pk):
    

    udata=User.objects.get(id=pk)
    cdata=Customer.objects.get(user_id=udata)
    user_id2=request.POST['id']
    product = House.objects.get(id=user_id2)
    address=request.POST['address']
    rent= request.POST['rent']
    roomno=request.POST['roomno']
    image=request.POST['image']
    newcart=Cart.objects.create(user_id2=product,user_id=cdata,Address=address,Rent=rent,Roomno=roomno,Image=image)
    all_data1 = getallcart(request,pk)
    return render(request,"app/cart.html",{'key3':all_data1[0], 'sub_total': all_data1[1]})

def getallcart(request,pk):
    udata = User.objects.get(id=pk)
    sub_total = 0
    if udata.Role=="Customer":
        customer = Customer.objects.get(user_id=udata)
        all_data1=Cart.objects.all().filter(user_id=customer)
        for t in all_data1:
            sub_total += int(t.Rent)
        print(sub_total)
        return all_data1, sub_total
        #return render(request,"app/cart.html",{'key3':all_data1})

def cartpage(request,pk):
    all_data1 = getallcart(request, pk)
    return render(request,"app/cart.html",{'key3':all_data1[0], 'sub_total': all_data1[1]})

def deletecart(request,pk):
    uid=request.POST['cid']  
    ddata=Cart.objects.get(id=uid)
    ddata.delete()
        
    url=f"/cart/{pk}"
    return redirect(url)



def Proceedtocheckout(request,pk):
    udata = User.objects.get(id=pk)
    sub_total = 0
    if udata.Role=="Customer":
        cdata = Customer.objects.get(user_id=udata)
        all_data1=Cart.objects.all().filter(user_id=cdata)
        for t in all_data1:
            sub_total += int(t.Rent)
        return render(request,"app/checkout.html",{'keyp':all_data1,'keyc':cdata,'sub_total':sub_total})




def logout(request):
    del request.session['id']
    del request.session['Email']
    del request.session['Role']
    del request.session['Firstname']
    return render(request,"app/index.html")



def initiate_payment(request):
    try:
        udata = User.objects.get(Email=request.session['Email'])
        amount = int(request.POST['sub_total'])
        #user = authenticate(request, username=username, password=password)
    except Exception as err:
        print(err)
        return render(request, 'app/checkout.html', context={'error': 'Wrong Accound Details or amount'})

    transaction = Transaction.objects.create(made_by=udata, amount=amount)
    transaction.save()
    merchant_key = settings.PAYTM_SECRET_KEY

    params = (
        ('MID', settings.PAYTM_MERCHANT_ID),
        ('ORDER_ID', str(transaction.order_id)),
        ('CUST_ID', str(transaction.made_by.Email)),
        ('TXN_AMOUNT', str(transaction.amount)),
        ('CHANNEL_ID', settings.PAYTM_CHANNEL_ID),
        ('WEBSITE', settings.PAYTM_WEBSITE),
        # ('EMAIL', request.user.email),
        # ('MOBILE_N0', '9911223388'),
        ('INDUSTRY_TYPE_ID', settings.PAYTM_INDUSTRY_TYPE_ID),
        ('CALLBACK_URL', 'http://127.0.0.1:8000/callback/'),
        # ('PAYMENT_MODE_ONLY', 'NO'),
    )

    paytm_params = dict(params)
    checksum = generate_checksum(paytm_params, merchant_key)

    transaction.checksum = checksum
    transaction.save()

    paytm_params['CHECKSUMHASH'] = checksum
    print('SENT: ', checksum)
    return render(request, 'app/redirect.html', context=paytm_params)


@csrf_exempt
def callback(request):
    if request.method == 'POST':
        received_data = dict(request.POST)
        paytm_params = {}
        paytm_checksum = received_data['CHECKSUMHASH'][0]
        for key, value in received_data.items():
            if key == 'CHECKSUMHASH':
                paytm_checksum = value[0]
            else:
                paytm_params[key] = str(value[0])
        # Verify checksum
        is_valid_checksum = verify_checksum(paytm_params, settings.PAYTM_SECRET_KEY, str(paytm_checksum))
        if is_valid_checksum:
            received_data['message'] = "Checksum Matched"
        else:
            received_data['message'] = "Checksum Mismatched"
            return render(request, 'app/callback.html', context=received_data)
        return render(request, 'app/callback.html', context=received_data)

def returnhome(request):
    return render(request,"app/index-1.html")



#forget password
otp=0

def forgotpassword(request):
    return render(request,"app/forgetpassword.html")

   
def sendpassword(request):
    email=request.POST['email']
    
        
    user = User.objects.get(Email=email)
    if user:
        print("==user1=====")
        print(email)
        print("-----------")
        print(user.Email)
        if user.Email == email:

                    otp = randint(1000, 9999)
                    user.OTP=otp
                    user.save()
                    email_subject = "This is your new OTP"
                
                    sendmail(email_subject, 'mail_template', email, {'otp': otp})
                    return render(request,"app/resetpassword.html")
                    
        else:
                message = 'This email does not match'
                return render(request, "app/forgetpassword.html", {'msg': message})
    else:
            message = 'This email is not available'
            return render(request, "app/forgetpassword.html", {'msg': message})
   
def updatepassword(request):
    email = request.POST['email']
    password = request.POST['password']
    cpassword=request.POST['cpassword']
    otp1=request.POST['otp']
    user = User.objects.get(Email=email)
    
    if user:
        
        if user.Email == email:
            
            if password == cpassword :
                    print(user.Password)
                    print(otp1)
                    print(user.OTP)
                    print(request.POST['password'])
                    a=user.OTP==int(otp1) 
                    print(a)
                    if user.OTP==int(otp1) :
                        print('hello ')
                        user.Password = request.POST['password']
                        print(user.Password)
                        user.save()
                    else :
                        message='Wrong OTP '
                    
                    
            else:
                    message = 'password and confim password doesnot match or OTP is Wrong'
                    return render(request, "app/forgetpassword.html", {'msg': message})
        else:
                message = 'This email does not match'
                return render(request, "app/forgetpassword.html", {'msg': message})
    else:
            message = 'This email is not available'
            return render(request, "app/forgetpassword.html", {'msg': message})
    message="Your Password is Reset Sucessfuly"
    return render(request, "app/login.html", {'msg': message})






#website admin
def adminhomepage(request):
    pdata=House.objects.all()
    l2=len(pdata)
    return render(request,"website_admin/dashboard.html",{'l2':l2,'all':pdata})

def Accept(request,pk):
    hdata=House.objects.get(id=pk)
    hdata.Status=1
    hdata.save()
    pdata=House.objects.all()
    l2=len(pdata)
    
    return render(request,"website_admin/dashboard.html",{'l2':l2,'all':pdata})

    
def Denied(request,pk):
    hdata=House.objects.get(id=pk)
    hdata.Status=0
    hdata.save()
    pdata=House.objects.all()
    l2=len(pdata)
    return render(request,"app/website_admin/basic-table.html",{'sdata':sdata})

'''def allcustomer(request):
    cdata=Customer.objects.all()
    return render(request,"app/website_admin/basic-table2.html",{'cdata':cdata})

def allproduct(request):
    pdata=Product.objects.all()
    return render(request,"app/website_admin/basic-table-3.html",{'pdata':pdata})



def deleteorder(request,pk):
    odata=Transaction.objects.get(id=pk)
    odata.delete()
    all_order=Transaction.objects.all()
    return render(request,"app/website_admin/dashboard.html",{'all_order':all_order})



def deleteseller(request,pk):
    sdata=Seller.objects.get(id=pk)
    sdata.delete()
    all_seller=Seller.objects.all()
    return render(request,"app/website_admin/basic-table.html",{'all_seller':all_seller})

def deletecustomer(request,pk):
    cdata=Customer.objects.get(id=pk)
    cdata.delete()
    cdata=Customer.objects.all()
    return render(request,"app/website_admin/basic-table2.html",{'cdata':cdata})

    
def deleteproduct(request,pk):
    pdata=Product.objects.get(id=pk)
    pdata.delete()
    pdata=Product.objects.all()
    return render(request,"app/website_admin/basic-table-3.html",{'pdata':pdata})'''




    
    
