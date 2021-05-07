from django.template.response import TemplateResponse
from django.views import View
from django.http import HttpResponse

class DemoView(View):
    def get(self, request):
        print(request.scheme)
        print(request.scheme)
        return HttpResponse("<p>hi</p>")

    def index(request):
        context = {
            "name" : "neo"
        }
        return TemplateResponse(request, 'demo/index.html', context=context)

