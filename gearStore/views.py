from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from gearStore.forms import UserForm, UserProfileForm
from gearStore.models import UserProfile, Category
#from gearStore.forms import UserForm, UserProfileForm


# Create your views here.
def index(request):
    context_dict = {}
    context_dict['boldmessage'] = 'This is the Bold Message'
    if request.user.is_authenticated:
        context_dict["user_profile"] = UserProfile.objects.get(user=request.user)
    else:
        context_dict["user_profile"] = None
    context_dict["categories"] = Category.objects.all()
    return render(request, 'gearStore/index.html', context_dict)

def view_category(request, category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug = category_name_slug)
    except Category.DoesNotExist:
        #Redirect to home page if category doesn't exist
        return redirect(reverse("gearStore:index"))
    context_dict["category"] = category
    context_dict["gear_list"] = Gear.object.filter(category = category)
    return render(request, 'gearStore/view_category.html', context_dict)

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = UserProfile()
            profile.user = user
            profile.save()
            registered = True
        else:
            print("")
            print(user_form.errors)
    else:
        user_form = UserForm()

    if registered:
        return render(request, 'gearStore/login.html')
    
    return render(request, 'gearStore/register.html', context={'user_form':user_form, 'registered':registered})

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('gearStore:index'))
            else:
                return HttpResponse("Your Gear Store account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied")
    else:
        return render(request, 'gearStore/login.html')

def about(request):
    return render(request, 'gearStore/about.html')

def contact(request):
    return render(request, 'gearStore/contact.html')

def category_menu(request):
    context_dict = {}
    context_dict['categories'] = Category.objects.all()
    return render(request, 'gearStore/category_menu.html', context_dict)

@login_required
def account(request):
    return render(request, 'gearStore/account.html')

@login_required
def process_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)
    # Take the user back to the homepage.
    return redirect(reverse('gearStore:index'))