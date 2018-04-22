from django.shortcuts import render
from django.views.generic import View
from django.http.response import HttpResponse

from .models import Medlem
# Create your views here.
class Home(View):
    medlemmer = Medlem.objects.all()
    template_name = 'organizer/home.html'
    def get(self, request):
        return render(request, self.template_name, {'medlemmer':self.medlemmer})

class ProsjektSkisse(View):
    template_name = 'organizer/skisse.html'
    def get(self, request):
        return render(request, self.template_name, {})

class ProsjektBeskrivelse(View):
    template_name = 'organizer/beskrivelse.html'
    def get(self, request):
        return render(request, self.template_name, {})

class ProsjektDocs(View):
    template_name = 'organizer/docs.html'
    def get(self, request):
        return render(request, self.template_name, {})

class ProsjektStatus(View):
    template_name = 'organizer/status.html'
    def get(self, request):
        return render(request, self.template_name, {})
