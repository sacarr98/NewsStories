from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Profile, News
from .forms import NewsForm, SignUpForm, ProfilePicForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


def home(request):
    if request.user.is_authenticated:
        form = NewsForm(request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                news = form.save(commit=False)
                news.user = request.user
                news.save()
                messages.success(request, ("Your Post Has Been Shared"))
                return redirect('home')
        
        news = News.objects.all().order_by("-created_at")
        return render(request, 'home.html', {"news":news, "form":form})
    else:
        news = News.objects.all().order_by("-created_at")
        return render(request, 'home.html', {"news":news})


def profile_list(request):
    if request.user.is_authenticated:
        profiles = Profile.objects.exclude(user=request.user)
    else:
        messages.success(request, ("Please log in to view this page"))
        return redirect('home')

    return render(request, 'profile_list.html', {"profiles":profiles})


def unfollow(request, pk):
    if request.user.is_authenticated:
        # Find profile to unfollow
        profile = Profile.objects.get(user_id=pk)
        # unfollow selected user
        request.user.profile.follows.remove(profile)
        # save changes to followers
        request.user.profile.save
        # unfollow message
        messages.success(request, (f"{profile.user.username} has been unfollowed"))
        return redirect(request.META.get("HTTP_REFERER"))
    else:
        messages.success(request, ("Please log in to view this page"))
        return redirect('home')


def profile(request, pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=pk)
        news = News.objects.filter(user_id=pk).order_by("-created_at")

        # form
        if request.method == "POST":
            # Get user
            current_user_profile = request.user.profile
            # Get form data
            action = request.POST['follow']
            # follow or unfollow a user
            if action == "unfollow":
                current_user_profile.follows.remove(profile)
            elif action == "follow":
                current_user_profile.follows.add(profile)
            # Save changes to profile
            current_user_profile.save()

    else:
        messages.success(request, ("Please log in to view this page"))
        return redirect('home')

    return render(request, "profile.html", {"profile":profile, "news":news})

    
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You have been logged in"))
            return redirect('home')
        else:
            messages.success(request, ("Error logging in, please try again"))
            return redirect('login')
    
    else:
        return render(request, "login.html", {})


def logout_user(request):
    logout(request)
    messages.success(request, ("You have been logged out successfully"))
    return redirect('home')


def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            # log in the user
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Thanks for signing up! Welcome to Your News!"))
            return redirect('home')
            
    return render(request, "register.html", {'form':form})


def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        profile_user = Profile.objects.get(user__id=request.user.id)
        # Get Forms
        user_form = SignUpForm(request.POST or None, request.FILES or None, instance=current_user)
        profile_form = ProfilePicForm(request.POST or None, request.FILES or None, instance=profile_user)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            login(request, current_user)
            messages.success(request, ("Your Profile Has Been Updated"))
            return redirect('home')
        return render(request, "update_user.html", {'user_form':user_form, 'profile_form':profile_form})
    
    else:
        messages.success(request, ("Please Log in To View This Page"))


def news_like(request, pk):
    if request.user.is_authenticated:
        news = get_object_or_404(News, id=pk)
        if news.likes.filter(id=request.user.id):
            news.likes.remove(request.user)
        else:
            news.likes.add(request.user)
        return redirect(request.META.get("HTTP_REFERER"))
    else:
        messages.success(request, ("Please log in to use this action"))
        return redirect('home')


def news_display(request, pk):
    news = get_object_or_404(News, id=pk)
    if news:
        return render(request, "news_display.html", {'news':news})

    else:
        messages.success(request, ("News story not available"))
        return redirect('home')


def delete_post(request, pk):
    if request.user.is_authenticated:
        news = get_object_or_404(News, id=pk)
        # check if post belongs to user
        if request.user.username == news.user.username:
            # delete post
            news.delete()
            messages.success(request, ("Post successfully deleted"))
            return redirect(request.META.get("HTTP_REFERER"))
        else:
            return redirect(request.META.get("HTTP_REFERER"))
    else:
        messages.success(request, ("Please log in to use this action"))
        return redirect(request.META.get("HTTP_REFERER"))


def edit_post(request, pk):
    if request.user.is_authenticated:
        # find selected post
        news = get_object_or_404(News, id=pk)
    # check if post belongs to user
        if request.user.username == news.user.username:
            form = NewsForm(request.POST or None, instance=news)
            if request.method == "POST":
                if form.is_valid():
                    news = form.save(commit=False)
                    news.user = request.user
                    news.save()
                    messages.success(request, ("Your Post Has Been Updated"))
                    return redirect('home')
            else:
                return render(request, "edit_post.html", {'form':form, 'news':news})
        else:
            messages.success(request, ("You can only edit your own posts"))
            return redirect('home')
    else:
        messages.success(request, ("Please log in to use this action"))
        return redirect('home')


def search(request):
    if request.method == "POST":
        # get value entered into form field
        search = request.POST['search']
        # search database for value entered
        searched = News.objects.filter(body__contains = search)
        return render(request, 'search.html', {'search':search, 'searched':searched})

    else:
        return render(request, 'search.html', {})


def search_user(request):
    if request.method == "POST":
        # get username entered into form field
        search = request.POST['search']
        # search database for username entered
        searched = User.objects.filter(username__contains = search)
        return render(request, 'search_user.html', {'search':search, 'searched':searched})

    else:
        return render(request, 'search_user.html', {})