from django.shortcuts import render, get_object_or_404
from django.views.generic import View

from .models import Post
from organizer.models import Medlem
# Create your views here.
class Landing(View):
    template_name = 'dagbok/landing.html'
    medlemmer = Medlem.objects.all()
    def get(self, request):
        return render(
            request,
            self.template_name,
            {'medlemmer':self.medlemmer}
        )
class Dagbok(View):
    template_name = 'dagbok/dagbok.html'
    def get(self, request, slug):
        medlem = get_object_or_404(Medlem, slug=slug)
        return render( request, self.template_name, {'medlem':medlem} )
