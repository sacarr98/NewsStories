from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Profile


def home(request):
    return render(request, 'home.html', {})


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

    return render(request, "profile.html", {"profile":profile})

    
