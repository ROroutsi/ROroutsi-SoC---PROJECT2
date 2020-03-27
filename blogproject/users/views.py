from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import DeleteView, CreateView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from .forms import UserRegisterForm

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Account created! You can now login!')
			return redirect('login')
	else:
		form = UserRegisterForm()
	return render(request, 'users/register.html', {'form' : form})			

@login_required
def profile(request):
	return render(request, 'users/profile.html')

class delete(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
	model = User
	success_url = "/login"
	success_message = 'Your account has been deleted!'
