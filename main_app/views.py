#from django.http import HttpResponse

#def homeView(request):
    #return HttpResponse("<h1>Hello World</h1>")

from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name= "index.html"
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