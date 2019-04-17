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
    #def getDAta(request):
        #getdata=Quote.objects.all()
        #context={
        #   'getdata': getdata}
        ## return render(request, 'index.html', context) 
    def deleteq(request, id):
        datadel=Quote.objects.get(pk=id)
        datadel.delete()
        return redirect('/')
    def editq(request, id):
        datae=Quote.objects.get(pk=id)
        datae1=QuoteCatergory.objects.all()
        context={
            'datae':datae, 'datae1':datae1
        }
        return render(request, 'edit.html', context)
    def updateq(request, id):
        datau=Quote.objects.get(pk=id)
        datau.quote=request.POST['quote']
        datau.author=request.POST['author']
        datau.date=request.POST['date']
        datau.quotecatergory.title=request.POST['title']
        datau.save()
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


class AboutView(TemplateView):
    template_name="about.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pagename']="About"
        context['h_active']=""
        context['a_active']="active"
        return context