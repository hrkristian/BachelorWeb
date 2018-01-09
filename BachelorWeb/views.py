from django.shortcuts import redirect
from django.shortcuts import (get_object_or_404, render)

def redirect_root(request):
    return redirect('home')
