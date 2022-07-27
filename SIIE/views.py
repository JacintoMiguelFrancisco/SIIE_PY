from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

@login_required
def index (request):
    return render(request, 'index.html')

class Error404View (TemplateView):
    template_name = 'Errors/error_404.html'

class Error500View (TemplateView):
    template_name = 'Errors/error_500.html'

    @classmethod
    def as_error_view(cls):

        v = cls.as_view()
        def view(request):
            r = v(request)
            r.render()
            return r
        return view