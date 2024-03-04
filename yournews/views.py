from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Profile, News
from .forms import NewsForm
from django.contrib.auth import authenticate, login, logout


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