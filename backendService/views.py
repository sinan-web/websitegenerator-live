from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import CustomerData
from .forms import CreateUserForm
from .decorator import allowed_users


# Create your views here.
def customerData(request):
   if request.method == "POST":
       data = CustomerData()
       data.user = request.user
       data.customerName = request.POST.get("customerName")
       data.companyName = request.POST.get("companyName")
       data.aboutUsText = request.POST.get("aboutUsText")
       data.image1 = request.FILES.get("image1")
       data.image2 = request.FILES.get("image2")
       data.image3 = request.FILES.get("image3")
       data.adress = request.POST.get("adress")
       data.telephone = request.POST.get("telephone")
       data.email = request.POST.get("email")
       data.save()
       return HttpResponse("Websitedaten erfolgreich angelegt")

   return render (request, "customerData.html")

@allowed_users(allowed_roles=[ "admin", "customer"])
def customerHomepage (request):
    data = CustomerData()
    homedirectory = request.user.customerdata.template
    customersData = request.user.customerdata
    return render (request, homedirectory, {"customersData": customersData})

@allowed_users(allowed_roles=["customer", "admin"])
def templateOne (request):
    customersData = request.user.customerdata
    return render (request, "templateOne.html", {"customersData": customersData})

@allowed_users(allowed_roles=["customer", "admin"])
def templateTwo (request):
    customersData = request.user.customerdata
    return render (request, "templateTwo.html", {"customersData": customersData})

@allowed_users(allowed_roles=["customer", "admin"])
def templateThree (request):
    customersData = request.user.customerdata
    return render (request, "templateThree.html", {"customersData": customersData})


def registerPage(request):
        form = CreateUserForm(request.POST)
        if request.method == "POST":
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get("username")
                messages.success(request, "Nutzer erfolgreich erstellt " + user) 
                return redirect("login")
        if request.user.is_authenticated:
            return redirect("/")
        context = {"form": form}
        return render (request,"account/register.html", context)

def loginPage(request):
		if request.method == "POST":
			username = request.POST.get("username")
			password =request.POST.get("password")

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect("mypage")
			else:
				messages.info(request, "Username OR password is incorrect")
		context = {}
		return render(request, "account/login.html", context)

def logoutUser(request):
    logout(request)
    return redirect("login")

@allowed_users(allowed_roles=["customer", "admin"])
def Templateselection (request):
    t = request.user.customerdata
    if request.method == "POST":
        t.template = request.POST.get("templateselection")
        t.save()
        return redirect("mypage")
    context = {"t": t}    
    return render (request, "templateSelection.html", context)

def Homepage (request):
    return render(request, "home.html")