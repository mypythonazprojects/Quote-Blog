#from django.http import HttpResponse

#def homeView(request):
    #return HttpResponse("<h1>Hello World</h1>")
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic import ListView
from . models import Quote
from . models import QuoteCatergory

class HomeView(ListView):
    template_name= "index.html"
    model=Quote
    #getdata=Quote.objects.all()
    def deleteq(request, id):
        datadel=Quote.objects.get(pk=id)
        datadel.delete()
        return redirect('/')


    def get_queryset(self):
        queryset=super().get_queryset()
        return queryset.select_related('quotecatergory')  #getting the foreign key values

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['myname'] = "azad"   #sending data to index.html
        list=[1, 2, 3, 4]
        context['list']=list
        context['pagename']="Home"
        context['h_active']="active"
        context['a_active']=""
        return context
   # return render(request, 'index.html', {'books':books})


class AboutView(TemplateView):
    template_name="about.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pagename']="About"
        context['h_active']=""
        context['a_active']="active"
        return context