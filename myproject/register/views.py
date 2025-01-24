from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


# Create your models here.
def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("posts:list")
    else:
        form = UserCreationForm()
        
    return render(request,'register/register.html', {"form":form})