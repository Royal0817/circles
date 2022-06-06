from django.views.generic.base import TemplateView
# from django.views.generic.edit import CreateView,UpdateView,DeleteView

class Home(TemplateView):
    template_name = 'base.html'
 