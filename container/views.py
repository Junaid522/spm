from django.shortcuts import render

# Create your views here.
from django.views import View


class ContainerDetails(View):

    template_name = 'container_details.html'

    def get(self, request, *args, **kwargs):
        return render(request, template_name=self.template_name)


class WarehouseDetails(View):

    template_name = 'warehouse_details.html'

    def get(self, request, *args, **kwargs):
        return render(request, template_name=self.template_name)


class Bilties(View):

    template_name = 'bilties.html'

    def get(self, request, *args, **kwargs):
        return render(request, template_name=self.template_name)