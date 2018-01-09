from django.shortcuts import render
from django.views.generic import View
from django.http.response import HttpResponse

# Create your views here.
class Home(View):
    template_name = 'organizer/home.html'
    medlemmer = ['Kristian Robertsen', 'Atle Amundsen', 'Nikolai Fosså']
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
