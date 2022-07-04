from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

@login_required
def index (request):
    return render(request, 'index.html')

class Error404View (TemplateView):
    template_name = 'Errors/error_404.html'