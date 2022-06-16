from django.shortcuts import render
from django.views.generic import TemplateView

def index (request):
    return render(request, 'index.html')

class Error404View (TemplateView):
    template_name = 'Errors/error_404.html'