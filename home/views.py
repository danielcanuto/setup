from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "home/index.html"

class SobreView(TemplateView):
    template_name = "home/sobre.html"