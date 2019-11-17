from django.shortcuts import render
from django.views import View
# Create your views here.


class Home(View):
      template_name='home.html'

      def get(self,request,*args,**kwargs):
          return render(request,self.template_name)


class AboutUs(View):

    template_name = 'about_us.html'

    def get(self, request, *args, **kwargs):
        return render(request, template_name=self.template_name)


class ContactUs(View):

    template_name = 'contact_us.html'

    def get(self, request, *args, **kwargs):
        return render(request, template_name=self.template_name)