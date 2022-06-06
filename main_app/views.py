from curses.ascii import US
from django.shortcuts import render
from django.views.generic.base import TemplateView
# from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.shortcuts import redirect,render


def front(request):
    context = { }
    return render(request, 'index.html', context)

class Home(TemplateView):
    template_name = 'home.html'

# class Landing(TemplateView):
#     template_name = 'landingpage.html'
 
# class Signup(View):
#     def get(self, request):
#         form = UserCreationForm()
#         context = {'form': form}
#         return render(request, 'registration/signup.html', context)

#     def post(self, request):
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('/home')
#         else:
#             context = {'form: form'}
#             return render(request, 'registration/signup.html', context)