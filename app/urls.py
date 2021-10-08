from django.contrib import admin
from django.urls import path,include
from.import views
#from .views import initiate_payment, callback

urlpatterns = [
    #customer
    path("",views.indexpage,name="index"),
    path("Register",views.RegisterUser,name="register"),
    path("RegisterPage",views.RegisterPage,name="registerpage"),
    path("verify<int:otp>",views.verify,name="verify"),
    path("LoginPage",views.LoginPage,name="loginpage"),
    path("Login",views.LoginUser,name="login"),
    path('logout/',views.logout, name='logout'),
    path("forgetpassword",views.forgotpassword,name="forgetpassword"),
    path("sentpassword",views.sendpassword,name="sentpassword"),
    path("updatepassword",views.updatepassword,name="updatepassword"),
    path("CategoryProducts1/<str:name>",views.OpenCategory1,name="opencategory1"),
    path("Categorylocation1/<str:name>",views.OpenCategorylocation1,name="OpenCategorylocation1"),
    path("Categoryprice1/<str:price>",views.OpenCategoryforprice1,name="OpenCategoryprice1"),
    path("house-details1/<int:pk>",views.showhousedetail1,name="housedetails1"),
    
    




    path("CategoryProducts/<str:name>",views.OpenCategory,name="opencategory"),
    path("Categorylocation/<str:name>",views.OpenCategorylocation,name="OpenCategorylocation"),
    path("Categoryprice/<str:price>",views.OpenCategoryforprice,name="OpenCategoryprice"),

    path("house-details/<int:pk>",views.showhousedetail,name="housedetails"),
    path("addtocart/<int:pk>",views.addtoCart,name="addtocart"),
    path("cart/<int:pk>",views.cartpage,name="cart"),
    path("deletecart/<int:pk>",views.deletecart,name="deletecart"),


    #owner
    path("ownerindex/",views.ownerindexpage,name="ownerindex"),
    path("form/",views.HouseFormPage,name="houseform"),
    path("showprofile/<int:pk>",views.ShowProfile,name="showprofile"),
    path("updateprofile/<int:pk>",views.UpdateData,name="updateprofile"),
    path("houselist/",views.getAllHouse,name="allhouse"),
    path("edithouse/<int:pk>",views.EditDataById,name="edithouse"),
    path("updatehouse/<int:pk>",views.UpdateHouse,name="updatehouse"),
    path("deletehouse/<int:pk>",views.DeleteHouse,name="deletehouse"),
    


    path("addhouse/<int:pk>",views.AddHouse,name="addhouse"),

    #payment
    path("checkout/<int:pk>",views.Proceedtocheckout,name="checkout"),
    path('pay/',views.initiate_payment, name='pay'),
    path('callback/', views.callback, name='callback'),
    path("welcomeback/",views.returnhome,name="welcomeback"),



    #website admin
    path("adminpage/",views.adminhomepage,name="adminpage"),
    path("accept/<int:pk>",views.Accept,name="accept"),
    path("denied/<int:pk>",views.Denied,name="denied"),
    

    
]
