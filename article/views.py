from django.shortcuts import render,redirect,get_object_or_404,reverse

from .forms import ContactForm

from django.contrib import messages
from django.contrib.auth.decorators import login_required




def index(request):
	
	return render(request,"homepage.html")


def about(request):
	return render(request,"about.html")
def whitepeaper(request):
	return render(request,"whitepeaper.html")
def emailView(request):
	if request.method=="POST":
		form=ContactForm(request.POST)
		if form.is_valid():
			name=form.cleaned_data["name"]
			email=form.cleaned_data["email"]
			phone=form.cleaned_data["phone"]
			message=form.cleaned_data["message"]
			form.save()
			messages.success(request,"Mesaj Başarılı bir şekilde Gönderildi.")
			return redirect("index")
	else:
		form=ContactForm()
	return render(request,"contact.html",{"form":form})













